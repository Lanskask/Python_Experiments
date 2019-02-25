# Kwargs

def doubler(f):
	def g(x):
		return 2 * f(x)
	return g

def f1(x):
	return x + 1

g = doubler(f1)
print(g(3))
print(g(-1))

def f2(x, y): return x + y

def magic(*args, **kwargs):
	print("un named args: ", args)
	print("named args: ", kwargs)

magic(1, 2, key="word", key2="word2")


def doubler_correct(f):
	def g(*args, **kwargs):
		"Какими бы ни были агр-ты для g, передать их в f"
		return 2 * f(*args, **kwargs)
	return g

g = doubler_correct(f2)
print(g(1,2))