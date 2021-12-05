import requests
import xml.etree.ElementTree as ET
import json

# XML описание Москвы
response = requests.get(r'https://www.openstreetmap.org/api/0.6/relation/102269')
text = response.text

#xml_file = open("moscow.xml", "w", encoding="utf-8")
#xml_file.write(text)

root = ET.fromstring(text)
districts = []
for child in root.iter('member'):
    if child.get('type') == "relation":
        districts.append({'ref': child.get('ref'), 'name': '', 'childs': []})

for okr in range(len(districts)):
    response = requests.get(f'https://www.openstreetmap.org/api/0.6/relation/{districts[okr]["ref"]}')
    file = ET.fromstring(response.text)
    name = ''
    for tag in file.iter('tag'):
        if tag.get('k') == 'name':
            name = tag.get('v')
    districts[okr]['name'] = name
    for child in file.iter('member'):
        if child.get('type') == "relation":
            districts[okr]['childs'].append({'ref': child.get('ref'), 'name': '', 'points': []})


# save = open("moscow.json", "w")
# json.dump(districts, save, indent=4)

for okr in range(len(districts)):
    for dist in range(len(districts[okr]['childs'])):
        a = districts[okr]["childs"][dist]["ref"]
        response = requests.get(f'https://www.openstreetmap.org/api/0.6/relation/{a}')
        file = ET.fromstring(response.text)
        name = ''
        for tag in file.iter('tag'):
            if tag.get('k') == 'name':
                name = tag.get('v')
        districts[okr]['childs'][dist]['name'] = name

        for child in file.iter('member'):
            if child.get('type') == 'way':
                response = requests.get(f'https://www.openstreetmap.org/api/0.6/way/{child.get("ref")}')
                line = ET.fromstring(response.text)
                for ref in line.iter('nd'):
                    response = requests.get(f'https://www.openstreetmap.org/api/0.6/node/{ref.get("ref")}')
                    noda = ET.fromstring(response.text)
                    node = noda.find('node')
                    districts[okr]['childs'][dist]['points'].append({'ref': node.get('id'), 'coords':{'lat': node.get("lat"), 'lon': node.get("lon")}})


save = open("moscow.json", "w", encoding='utf-8')
json.dump(districts, save, indent=4, ensure_ascii=False)
