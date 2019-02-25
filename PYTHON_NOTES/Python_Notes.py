Python_Notes.txt


Python collections
defaultdict
ChainMap


# ----------
from typing import List

def fib(n: int) -> List[int]:
	fib1: int = 1
	fib2: int = 1
	res = []
	for _ in range(n):
		res.append(fib1)
		fib1, fib2 = fib2, fib1 + fib2
	return res


from collections iimport namedtuple

Person = namedtuple(
	"Person",
	["first_name", "last_name", "age"]
)
p = Person("Terrence", "Gilliam", 77)

from typing import NamedTuple

class person(NamedTuple):
	first_name: str
	last_name: str
	age: int = 42

p = Person("Terrence", "Giliam", 77)


# ------------

graph = {}

def add_edge(u, v):
	if u not in graph;
		graph[u] = []

def neighbours(u):
	return graph[u] if u in graph else []


 # ---------
def add_edge(u, v):
	graph.setdefault(u, []).append(v)

def neighbours(u):
	return graph.get(u, [])

