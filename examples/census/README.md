bench-impyla
============

Benchmarks for impyla

### 1 Convert BigML model to eliminate dictionaries

Convert the raw BigML model to something that can be compiled. This requires
eliminating the use of a dictionary to pass in the data points.

```bash
bin/process_bigml_model.py -i raw-models/model_100.py -o models/model_100.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_1000.py -o models/model_1000.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_1500.py -o models/model_1500.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_2000.py -o models/model_2000.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_500.py -o models/model_500.py -d raw-data/bigml_53168e4dd63708516d001938.csv
```

### 2 Replicate the input data set to make it more sizeable

The raw input data set contains 32561 rows. For meaningful benchmarking on a
cluster, we need more. We'll use PySpark to replicate the data set.

Using a PySpark shell on the cluster (after copying over the data):

```python
with open('/home/laserson/raw_data/bigml_53168e4dd63708516d001938.csv', 'r') as ip:
    ip.next() # burn header line
    raw = filter(lambda x: x != '', [line.strip() for line in ip])

single = sc.parallelize(raw, 5).map(lambda line: '\t'.join(line.split(',')))
replicated = single.flatMap(lambda x: [x]*15000)
replicated.saveAsTextFile('/user/laserson/bigml/census_text')
```

### 3 Run model scoring in Impala

Advantages:
fast
work on local machine

```python
from impala.dbapi import connect
from impala.udf import ship_udf, udf, FunctionContext, StringVal, IntVal

create_table_query = """
    CREATE EXTERNAL TABLE census_text (age INT, workclass STRING,
	    final_weight INT, education STRING, education_num INT,
	    marital_status STRING, occupation STRING, relationship STRING,
	    race STRING, sex STRING, hours_per_week INT, native_country STRING,
	    income STRING)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
    STORED AS TEXTFILE
    LOCATION '/user/laserson/bigml/census_text'
"""

score_obs_query = """
    SELECT DISTINCT predict_income(age, workclass, final_weight, education,
	    education_num, marital_status, occupation, relationship, race, sex,
	    hours_per_week, native_country, income) FROM census_text
"""

signature = StringVal(FunctionContext, IntVal, StringVal, IntVal, StringVal,
	IntVal, StringVal, StringVal, StringVal, StringVal, StringVal, IntVal,
	StringVal, StringVal)
predict_income = udf(signature)(predict_income)

ship_udf


import sys
from impala.dbapi import connect
from impala.udf import ship_udf, udf, FunctionContext, StringVal, IntVal
sys.path.append('/Users/laserson/repos/impyla/examples/census/models')
#from model_100 import predict_income
from model_500 import predict_income
#from model_2000 import predict_income
signature = StringVal(FunctionContext, IntVal, StringVal, IntVal, StringVal,
	IntVal, StringVal, StringVal, StringVal, StringVal, StringVal, IntVal,
	StringVal, StringVal)
predict_income = udf(signature)(predict_income)
conn = connect(host='bottou01-10g.pa.cloudera.com', port=21050)
cursor = conn.cursor()
cursor.execute('USE laserson')
ship_udf(cursor, predict_income, '/user/laserson/test-udf/census.ll', 'bottou01-10g.pa.cloudera.com', user='laserson', overwrite=True)






from model_100 import predict_income as predict_income_100
from model_2000 import predict_income as predict_income_2000

```


### 4 Run model scoring in PySpark

```python
ident = lambda x: x # do nothing for strings
types = (int, ident, int, ident, int, ident, ident, ident, ident, ident, int,
	ident, ident)
num_fields = len(types)

def parse_obs(line):
    fields = line.split('\t')
    parsed = tuple([types[i](fields[i]) for i in xrange(num_fields)])
    return parsed

observations = sc.textFile('/user/laserson/bigml/census_text').map(parse_obs)
# the None is where the FunctionContext would go; for Impala compatibility
predictions = observations.map(lambda tup: predict_income(*((None,) + tup)))
predictions.distinct().collect()
```
