
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

def update_light(current):
    ans = current
    if(current == 'green'): ans = 'yellow'
    elif(current == 'yellow'): ans = 'red'
    elif(current == 'red'): ans = 'green'
    return ans


def add_binary(a,b):
    return bin(a+b)[2:]

#  ---------------
def str_1_sum(str):
  sum = 0 
  for c in bin(str)[2:]: 
      if c == '1': 
          sum += 1
  return sum

def countBits(n):
    return bin(n).count("1")

def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

def countBits(n):
    ret = 0
    while n:
        ret += n & 1
        n >>= 1
    return ret

def countBits(n):
  return (n & 1) + countBits(n >> 1) if n else 0
#  ---------------