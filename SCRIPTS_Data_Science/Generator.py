# python

def lazy_range(n): 
  """ленивая версия последовательности range"""
  i = 0
  while i < n:
    yield i
    i += 1

# for x in lazy_range(5): print(x)

lazy_events_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

for x in lazy_events_below_20: print(x)
