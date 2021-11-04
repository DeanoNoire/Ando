import tm1637
from time import sleep
from multiprocessing import Process
import json



tm = tm1637.TM1637(clk=21,dio=20) #brana
tm2 = tm1637.TM1637(clk=6,dio=5)  #garáž

tm.brightness(val=2)
tm2.brightness(val=2)


sleepTime = 0.2
hodnota = 0

horniPul  = 0b00000110
spodniPul = 0b00110000
sCel      = 0b00110110

def write(obj,a,b,c,d):
    if(obj == "gate"):
        tm.write([a,b,c,d])
    if(obj == "garage"):
        tm2.write([a,b,c,d])
    sleep(sleepTime)


def reset(obj):
    if(obj == "gate"):
        tm.write([0,0,0,0])
    if(obj == "garage"):
        tm2.write([0,0,0,0])

   
def writeState(obj,zmena):
    reset(obj)
    if zmena == 3:
        write(obj,spodniPul,0,0,0)
        write(obj,sCel,0,0,0)
        write(obj,horniPul,spodniPul,0,0)
        write(obj,0,sCel,0,0)
        write(obj,0,horniPul,spodniPul,0)
        write(obj,0,0,sCel,0)
        write(obj,0,0,horniPul,spodniPul)
        write(obj,0,0,0,sCel)
        write(obj,0,0,0,horniPul)
        print("Změna "+obj +": Otevírání")

    
    if zmena == 4:
        write(obj,0,0,0,horniPul)
        write(obj,0,0,0,sCel)
        write(obj,0,0,horniPul,spodniPul)
        write(obj,0,0,sCel,0)
        write(obj,0,horniPul,spodniPul,0)
        write(obj,0,sCel,0,0)
        write(obj,horniPul,spodniPul,0,0)
        write(obj,sCel,0,0,0)
        write(obj,spodniPul,0,0,0)
        print("Změna "+obj +": Otevírání")


def checkState(movementDurration,obj,zmena):
    for x in range(movementDurration):
        writeState(obj,zmena)
        reset(obj)

