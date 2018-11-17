# MapRedFilter
from functools import partial

def double(x): 
  return x * 2

xs = [1,2,3,4]

twice_xs = [double(x) for x in xs]
print(twice_xs)

twice_xs2 = map(double, xs)
print("twice_xs2 = map(double, xs)")
print(twice_xs2)
for x in twice_xs2: print(x)


list_doubler = partial(map, double)
twice_xs3 = list_doubler(xs)
print("""list_doubler = partial(map, double)
twice_xs3 = list_doubler(xs)""")
print(twice_xs3)
for x in twice_xs3: print(x)

print("\nMAP")
def multiply(x, y): return x * y

products = map(multiply, [1, 2], [4, 5])
print("products = map(multiply, [1, 2], [4, 5])")
print(products)
for x in products: print(x)

print("\nREDUCE")
from functools import reduce
print("x_products = reduce(lambda x, y:  x * y, xs)")
x_products = reduce(lambda x, y:  x * y, xs)
print(x_products)
