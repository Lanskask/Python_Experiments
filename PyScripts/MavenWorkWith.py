# MavenWorkWith

import xml.etree.ElementTree as ET

file_name = 'settings.xml'

root = ET.parse(file_name).getroot()

print('Expertise Data:')

for elem in root:
   for subelem in elem:
      print(subelem.text)