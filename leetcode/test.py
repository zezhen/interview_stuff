import json


f = open('/Users/zezhen/Downloads/test.json')
 
data = json.load(f)

for name, obj in data.items():
	print(obj['id'], name)

f.close()