def predict_income(impala_function_context, age, workclass, final_weight, education, education_num, marital_status, occupation, relationship, race, sex, hours_per_week, native_country, income):
    """ Predictor for income from model/536030f60af5e8092c001612

	https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
    """
    leq50 = '<=50K'
    gt50= '>50K'
    if (marital_status is None):
	return leq50
    if (marital_status == 'Married-civ-spouse'):
	if (education_num is None):
	    return leq50
	if (education_num > 12):
	    if (hours_per_week is None):
		return gt50
	    if (hours_per_week > 31):
		if (age is None):
		    return gt50
		if (age > 28):
		    if (education_num > 13):
			if (age > 58):
			    return gt50
			if (age <= 58):
			    return gt50
		    if (education_num <= 13):
			if (occupation is None):
			    return gt50
			if (occupation == 'Exec-managerial'):
			    return gt50
			if (occupation != 'Exec-managerial'):
			    return gt50
		if (age <= 28):
		    if (age > 24):
			if (occupation is None):
			    return leq50
			if (occupation == 'Tech-support'):
			    return gt50
			if (occupation != 'Tech-support'):
			    return leq50
		    if (age <= 24):
			if (final_weight is None):
			    return leq50
			if (final_weight > 492053):
			    return gt50
			if (final_weight <= 492053):
			    return leq50
	    if (hours_per_week <= 31):
		if (sex is None):
		    return leq50
		if (sex == 'Male'):
		    if (age is None):
			return leq50
		    if (age > 29):
			if (age > 62):
			    return leq50
			if (age <= 62):
			    return leq50
		    if (age <= 29):
			return leq50
		if (sex != 'Male'):
		    if (final_weight is None):
			return gt50
		    if (final_weight > 264521):
			if (hours_per_week > 7):
			    return leq50
			if (hours_per_week <= 7):
			    return gt50
		    if (final_weight <= 264521):
			if (age is None):
			    return gt50
			if (age > 26):
			    return gt50
			if (age <= 26):
			    return leq50
	if (education_num <= 12):
	    if (education_num > 8):
		if (age is None):
		    return leq50
		if (age > 35):
		    if (hours_per_week is None):
			return leq50
		    if (hours_per_week > 33):
			if (education_num > 9):
			    return gt50
			if (education_num <= 9):
			    return leq50
		    if (hours_per_week <= 33):
			if (workclass is None):
			    return leq50
			if (workclass == 'Self-emp-inc'):
			    return gt50
			if (workclass != 'Self-emp-inc'):
			    return leq50
		if (age <= 35):
		    if (age > 24):
			if (occupation is None):
			    return leq50
			if (occupation == 'Exec-managerial'):
			    return leq50
			if (occupation != 'Exec-managerial'):
			    return leq50
		    if (age <= 24):
			if (hours_per_week is None):
			    return leq50
			if (hours_per_week > 45):
			    return leq50
			if (hours_per_week <= 45):
			    return leq50
	    if (education_num <= 8):
		if (age is None):
		    return leq50
		if (age > 36):
		    if (hours_per_week is None):
			return leq50
		    if (hours_per_week > 22):
			if (education_num > 5):
			    return leq50
			if (education_num <= 5):
			    return leq50
		    if (hours_per_week <= 22):
			return leq50
		if (age <= 36):
		    if (workclass is None):
			return leq50
		    if (workclass == 'Private'):
			if (age > 35):
			    return leq50
			if (age <= 35):
			    return leq50
		    if (workclass != 'Private'):
			if (occupation is None):
			    return leq50
			if (occupation == 'Machine-op-inspct'):
			    return gt50
			if (occupation != 'Machine-op-inspct'):
			    return leq50
    if (marital_status != 'Married-civ-spouse'):
	if (education_num is None):
	    return leq50
	if (education_num > 12):
	    if (age is None):
		return leq50
	    if (age > 27):
		if (hours_per_week is None):
		    return leq50
		if (hours_per_week > 43):
		    if (occupation is None):
			return leq50
		    if (occupation == 'Exec-managerial'):
			if (age > 41):
			    return gt50
			if (age <= 41):
			    return leq50
		    if (occupation != 'Exec-managerial'):
			if (education_num > 14):
			    return gt50
			if (education_num <= 14):
			    return leq50
		if (hours_per_week <= 43):
		    if (education_num > 14):
			if (age > 32):
			    return gt50
			if (age <= 32):
			    return leq50
		    if (education_num <= 14):
			if (age > 45):
			    return leq50
			if (age <= 45):
			    return leq50
	    if (age <= 27):
		if (hours_per_week is None):
		    return leq50
		if (hours_per_week > 38):
		    if (relationship is None):
			return leq50
		    if (relationship == 'Wife'):
			return gt50
		    if (relationship != 'Wife'):
			if (hours_per_week > 77):
			    return leq50
			if (hours_per_week <= 77):
			    return leq50
		if (hours_per_week <= 38):
		    return leq50
	if (education_num <= 12):
	    if (age is None):
		return leq50
	    if (age > 31):
		if (hours_per_week is None):
		    return leq50
		if (hours_per_week > 41):
		    if (education_num > 5):
			if (age > 53):
			    return leq50
			if (age <= 53):
			    return leq50
		    if (education_num <= 5):
			return leq50
		if (hours_per_week <= 41):
		    if (occupation is None):
			return leq50
		    if (occupation == 'Other-service'):
			if (relationship is None):
			    return leq50
			if (relationship == 'Wife'):
			    return leq50
			if (relationship != 'Wife'):
			    return leq50
		    if (occupation != 'Other-service'):
			if (occupation == 'Machine-op-inspct'):
			    return leq50
			if (occupation != 'Machine-op-inspct'):
			    return leq50
	    if (age <= 31):
		if (age > 21):
		    if (hours_per_week is None):
			return leq50
		    if (hours_per_week > 41):
			if (workclass is None):
			    return leq50
			if (workclass == 'Private'):
			    return leq50
			if (workclass != 'Private'):
			    return leq50
		    if (hours_per_week <= 41):
			if (education_num > 9):
			    return leq50
			if (education_num <= 9):
			    return leq50
		if (age <= 21):
		    if (education is None):
			return leq50
		    if (education == '7th-8th'):
			if (occupation is None):
			    return leq50
			if (occupation == 'Other-service'):
			    return leq50
			if (occupation != 'Other-service'):
			    return leq50
		    if (education != '7th-8th'):
			return leq50
