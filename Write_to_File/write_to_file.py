
filename = "newfile.txt"

myfile = open(filename, 'w')
for x in ['1', '2','3']:
	myfile.write(x + 'Written with Python\n')
 
myfile.close()
