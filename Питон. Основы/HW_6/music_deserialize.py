import json
import pickle


with open('group.json', 'r', encoding='UTF-8') as f:
    my_json = json.load(f, encoding='UTF-8')
    print(my_json)


with open('group.pickle', 'rb') as f:
    my_bytes = pickle.load(f, encoding='UTF-8')
    print(my_bytes)
