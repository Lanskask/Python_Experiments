from functools import partial

class A:
    x = 92

    def foo(self):
        pass


a = A()

print(vars(a))

print(a.x)

a.x = 62

print(vars(a))

print(a.x)
print(A.x)

# -----------
a.foo()
A.foo(a)
f = a.foo
g = partial(A.foo, a)
f()
g()
