# def mean(x_arr):
# 	result = 0
# 	for x in x_arr: result += x
# 	return  result / len(x_arr)

def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)

def mean(x):
	return sum(x) / len(x)

def de_mean(x): # differences between mean and value
	"""translate x by subtracting its mean (so the result has mean 0)"""
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]

def variance(x):
	"""assumes x has at least two elements"""
	n = len(x)
	deviations = de_mean(x)
	return sum_of_squares(deviations) / (n - 1)


num_friends = [1,5,7,2,8,9,3,6,77,2,4,6,8,43,8,9,44,8,90]

answer = variance(num_friends) # 81.54

print(mean(num_friends))
print(answer)

