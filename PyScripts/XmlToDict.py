import xmltodict
import pprint
import json

file_name = 'settings.xml'

with open(file_name) as fd:
	doc = xmltodict.parse(fd.read())

# print(doc)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(json.dumps(doc))