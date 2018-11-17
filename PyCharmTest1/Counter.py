class Counter:
    all_counters = []

    def __init__(self, initial_counter=0):
        Counter.all_counters.append(self)
        self.count = initial_counter

    def __repr__(self):
        return f'It\'s a Counter with {self.count}'

    def get(self):
        return self.count

    def increment(self):
        self.count += 1


c1 = Counter(initial_counter=91)
c2 = Counter(92)
c1.increment()

assert len(Counter.all_counters) == 2
print(len(Counter.all_counters) == 2)
assert c1.all_counters is c2.all_counters
print(c1.all_counters is c2.all_counters)

print(c1)
print(c1.get())
