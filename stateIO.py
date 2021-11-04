import json
from time import sleep
import dbChanger
import threading
import asyncio
#import display

#statesPath = '/home/pi/Ando/states.json'
statesPath = 'C:/Users/rykala/Ando/Ando/states.json'

def stateRead():
    json_file = open(statesPath,'r')
    data = json.load(json_file)
    print('Garage stav:'+str(data['garage']))
    print('Gate stav: '+str(data['gate']))
    return('State: garage='+str(data['garage'])+' gate='+str(data['gate']))

def stateReadJSON():
    json_file = open(statesPath,'r')
    data = json.load(json_file)
    print('Garage stav:'+str(data['garage']))
    print('Gate stav: '+str(data['gate']))
    return(data['garage'],data['gate'])


def stateChange(obj):
    #Čtení stavu
    json_file = open(statesPath, "r")
    data = json.load(json_file)
    obj_stav = data[obj]
    json_file.close()

    # Změna stavu
    obj_stav_novy = abs(obj_stav - 1)
    data[obj] = obj_stav_novy
    print("Změna"+str(obj)+" : z " +str(obj_stav)+" na "+str(obj_stav_novy)+", tedy dochází k "+str(obj_stav-obj_stav_novy))
    
    #Zavírání
    if(obj_stav-obj_stav_novy == 1):
        zapis(obj,4)
        dbChanger.zapisDb(obj,4)
        #display.checkState()
        th = threading.Thread(target=zapisNoveho,args=(obj,obj_stav_novy))
        th.start()

    #Otevírání
    if(obj_stav-obj_stav_novy == -1):
        zapis(obj,3)
        dbChanger.zapisDb(obj,3)
        #display.checkState()
        #cvaknutí relé zde
        th = threading.Thread(target=zapisNoveho,args=(obj,obj_stav_novy))
        th.start()
    
def zapisNoveho(obj,obj_stav_novy):
    #Zápis nového stavu po odmlce
    sleep(10)
    zapis(obj,obj_stav_novy)
    dbChanger.zapisDb(obj,obj_stav_novy)



def zapis(obj,stav):
    #Čtení stavu
    json_file = open(statesPath, "r")
    data = json.load(json_file)
    json_file.close()
    
    data[obj] = stav

    # Uložení stavu
    jsonFile = open(statesPath, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

