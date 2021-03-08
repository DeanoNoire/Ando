import json

def stateRead():
    with open('states.json') as json_file:
        data = json.load(json_file)
    print('Data:')
    print(data)
