import json

def stateRead():
    json_file = open('states.json','r')
    data = json.load(json_file)
    print('Garage stav:'+str(data['garage']))
    print('Gate stav: '+str(data['gate']))
    return('State: garage='+str(data['garage'])+' gate='+str(data['gate']))
    
def stateChange(obj):
    #Čtení stavu
    json_file = open("states.json", "r")
    data = json.load(json_file)
    obj_stav = data[obj]
    json_file.close()

    # Změna stavu
    obj_stav_novy = abs(obj_stav - 1)
    data[obj] = obj_stav_novy

    # Uložení nového stavu
    jsonFile = open("states.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

def stateReset(garage,gate):
    #Čtení stavu
    json_file = open("states.json", "r")
    data = json.load(json_file)
    json_file.close()

    data['garage'] = garage
    data['gate'] = gate

    # Uložení nového stavu
    jsonFile = open("states.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()