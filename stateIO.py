import json
from time import sleep

def stateRead():
    json_file = open('states.json','r')
    data = json.load(json_file)
    print('Garage stav:'+str(data['garage']))
    print('Gate stav: '+str(data['gate']))
    return('State: garage='+str(data['garage'])+' gate='+str(data['gate']))

def stateReadJSON():
    json_file = open('states.json','r')
    data = json.load(json_file)
    print('Garage stav:'+str(data['garage']))
    print('Gate stav: '+str(data['gate']))
    return(data['garage'],data['gate'])
    
def stateChange(obj):
    #Čtení stavu
    json_file = open("states.json", "r")
    data = json.load(json_file)
    obj_stav = data[obj]
    json_file.close()

    # Změna stavu
    obj_stav_novy = abs(obj_stav - 1)
    data[obj] = obj_stav_novy

    stateInProgress(obj,obj_stav_novy)
    sleep(5)

    # Uložení nového stavu
    jsonFile = open("states.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

def stateInProgress(obj,novyStav):
    #Čtení nového stavu
    json_file = open("states.json", "r")
    data = json.load(json_file)
    json_file.close()
    
    if novyStav == 1:
        data[obj] = 50
    elif novyStav == 0:
        data[obj] = 500


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