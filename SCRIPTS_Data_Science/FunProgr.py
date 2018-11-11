# Fun Progr

from functools import partial

def exp(base, power):
	return base ** power

def two_to_the(power):
	return exp(2, power)

two_to_the = partial(exp, 2)

print(two_to_the(3))


# or


square_of = partial(exp, power=2)

print(square_of(3))