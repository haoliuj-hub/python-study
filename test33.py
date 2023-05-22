"""
json
"""

import json

data = [{'name': '刘昊', 'age': 11}, {'name': 'B', 'age': 12}, {'name': 'C', 'age': 13}]

json_str = json.dumps(data)
print(type(json_str))
print(json_str)

json_str2 = json.dumps(data, ensure_ascii=False)
print(json_str2)

data2 = {'name': '刘昊2', 'age': 11}

json_str3 = json.dumps(data2, ensure_ascii=False)
print(json_str3)

dict1 = json.loads(json_str3)
print(type(dict1))
print(dict1)

list1 = json.loads(json_str)
print(type(list1))
print(list1)

