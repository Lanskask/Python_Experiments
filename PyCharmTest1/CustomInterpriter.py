def eval(code):
	env = {}
	stack = []
	for line in code.strip().splitlines():
		op, *args = line.split()
		print(f"env : {env}\n\stack: {stack}\n")
		if op == "LOAD_CONST":
			stack.append(int(args[0]))
		elif op == "STORE_NAME":
			env[args[0]] = stack.pop()
		elif op == "LOAD_NAME":
			stack.append(env[args[0]])
		elif op == "BINARY_ADD":
			stack.append(stack.pop() + stack.pop())
		else:
			assert False, f"unknown op: {op[0]}"
	print(f"env: {env}\nstack: {stack}\n")


eval("""
LOAD_CONST 30
STORE_NAME x
LOAD_CONST 62
STORE_NAME y
LOAD_NAME x
LOAD_NAME y
BINARY_ADD 
STORE_NAME z
""")
