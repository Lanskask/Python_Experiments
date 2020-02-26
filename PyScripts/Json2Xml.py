import json
import xmltodict
 

inp_file_name = "settings.json"
outp_file_name = "result_settings.xml"

with open(inp_file_name, 'r') as f:
    jsonString = f.read()
 
print(f"JSON input ({inp_file_name}):")
print(jsonString)
 
xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
 
print(f'\nXML output({outp_file_name}.xml):')
print(xmlString)
 
with open('output.xml', 'w') as f:
    f.write(xmlString)