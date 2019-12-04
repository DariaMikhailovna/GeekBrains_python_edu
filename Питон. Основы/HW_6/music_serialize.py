import json
import pickle


my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]
}


my_json = json.dumps(my_favourite_group)
print(my_json)

my_bytes = pickle.dumps(my_favourite_group)
print(my_bytes)

with open('group.json', 'w', encoding='UTF-8') as f:
    json.dump(my_favourite_group, f)


with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
