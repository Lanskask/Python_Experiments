class Counter:
    all_counters = []

    def __init__(self, initial_counter=0):
        Counter.all_counters.append(self)
        self._count = initial_counter

    def __repr__(self):
        return f'It\'s a Counter with {self._count}'

    @property
    def count(self):
        return self._count

    @property
    def get(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @count.deleter
    def count(self):
        print("It's deleter of c4")
        del self._count

    @property
    def is_zero(self):
        return self._count == 0 

    def increment(self):
        self._count += 1


c1 = Counter(initial_counter=91)
c2 = Counter(92)
c1.increment()

assert len(Counter.all_counters) == 2
print(len(Counter.all_counters) == 2)
assert c1.all_counters is c2.all_counters
print(c1.all_counters is c2.all_counters)

print(c1)
print(c1.get)

print(c1.is_zero)


