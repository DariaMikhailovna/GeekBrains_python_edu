import json
import re
import os

def change(config):
    config['a'][0] = 0.1


def apply_format(my_json, data):
    print(repr(my_json))
    print(repr(data))
    t = re.findall(r'[\s{}(),:]+', data)
    c = len(t)
    for j in c:      
        for i, x in enumerate(my_json):
            tt = 0
            if tt == j:
                break
            if x == ':' or x == '{' or x == '}' or x == ',' or '(' or ')':
                tt += 1
        my_json = my_json[:i] + t[c] + my_json[i:]

    print(t)
    return my_json


with open('in.json', 'r', encoding='UTF-8') as f:
    data = f.read()
my_json = json.loads(data)
change(my_json)
my_json = json.dumps(my_json)
my_json = apply_format(my_json, data)
with open('out.json', 'w', encoding='UTF-8') as f:
    f.write(my_json)

