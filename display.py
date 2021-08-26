import tm1637
from time import sleep
from multiprocessing import Process
import json



tm = tm1637.TM1637(clk=21,dio=20) #brana
tm2 = tm1637.TM1637(clk=6,dio=5)  #garáž

tm.brightness(val=2)
tm2.brightness(val=2)


sleepTime = 0.2
loops = 5
hodnota = 0

horniPul  = 0b00000110
spodniPul = 0b00110000
sCel      = 0b00110110

def garazWrite(a,b,c,d):
    tm.write([a,b,c,d])
    sleep(sleepTime)

def branaWrite(a,b,c,d):
    tm2.write([a,b,c,d])
    sleep(sleepTime)

def obojeWrite(a,b,c,d,e,f,g,h):
    tm.write([a,b,c,d])
    tm2.write([e,f,g,h])
    sleep(sleepTime)



def obojeReset():
        tm.write([0,0,0,0])
        tm2.write([0,0,0,0])

def stateReadDisplay():
    json_file = open('/home/pi/Ando/states.json','r')
    data = json.load(json_file)
    return data['garage'],data['gate']
    
def writeState(garaz,brana):
    obojeReset()
    if garaz == 50 and brana < 50:
        garazWrite(spodniPul,0,0,0)
        garazWrite(sCel,0,0,0)
        garazWrite(horniPul,spodniPul,0,0)
        garazWrite(0,sCel,0,0)
        garazWrite(0,horniPul,spodniPul,0)
        garazWrite(0,0,sCel,0)
        garazWrite(0,0,horniPul,spodniPul)
        garazWrite(0,0,0,sCel)
        garazWrite(0,0,0,horniPul)
        print("Změna garáž: Otevírání")

    elif garaz == 500 and brana < 50: 
        garazWrite(0,0,0,horniPul)
        garazWrite(0,0,0,sCel)
        garazWrite(0,0,horniPul,spodniPul)
        garazWrite(0,0,sCel,0)
        garazWrite(0,horniPul,spodniPul,0)
        garazWrite(0,sCel,0,0)
        garazWrite(horniPul,spodniPul,0,0)
        garazWrite(sCel,0,0,0)
        garazWrite(spodniPul,0,0,0)
        print("Změna garáž: Zavírání")


    elif garaz < 50 and brana == 50:
        branaWrite(spodniPul,0,0,0)
        branaWrite(sCel,0,0,0)
        branaWrite(horniPul,spodniPul,0,0)
        branaWrite(0,sCel,0,0)
        branaWrite(0,horniPul,spodniPul,0)
        branaWrite(0,0,sCel,0)
        branaWrite(0,0,horniPul,spodniPul)
        branaWrite(0,0,0,sCel)
        branaWrite(0,0,0,horniPul)
        print("Změna brana: Otevírání")

    elif garaz < 50 and brana == 500: 
        branaWrite(0,0,0,horniPul)
        branaWrite(0,0,0,sCel)
        branaWrite(0,0,horniPul,spodniPul)
        branaWrite(0,0,sCel,0)
        branaWrite(0,horniPul,spodniPul,0)
        branaWrite(0,sCel,0,0)
        branaWrite(horniPul,spodniPul,0,0)
        branaWrite(sCel,0,0,0)
        branaWrite(spodniPul,0,0,0)
        print("Změna brána: Zavírání")

    elif garaz == 50 and brana == 50:
        obojeWrite(spodniPul,0,0,0,spodniPul,0,0,0)
        obojeWrite(sCel,0,0,0,sCel,0,0,0)
        obojeWrite(horniPul,spodniPul,0,0,horniPul,spodniPul,0,0)
        obojeWrite(0,sCel,0,0,0,sCel,0,0)
        obojeWrite(0,horniPul,spodniPul,0,0,horniPul,spodniPul,0)
        obojeWrite(0,0,sCel,0,0,0,sCel,0)
        obojeWrite(0,0,horniPul,spodniPul,0,0,horniPul,spodniPul)
        obojeWrite(0,0,0,sCel,0,0,0,sCel)
        obojeWrite(0,0,0,horniPul,0,0,0,horniPul)
        print("Změna oboje: Otevírání")

    elif garaz == 500 and brana == 500:
        obojeWrite(0,0,0,horniPul,0,0,0,horniPul)
        obojeWrite(0,0,0,sCel,0,0,0,sCel)
        obojeWrite(0,0,horniPul,spodniPul,0,0,horniPul,spodniPul)
        obojeWrite(0,0,sCel,0,0,0,sCel,0)
        obojeWrite(0,horniPul,spodniPul,0,0,horniPul,spodniPul,0)
        obojeWrite(0,sCel,0,0,0,sCel,0,0)
        obojeWrite(horniPul,spodniPul,0,0,horniPul,spodniPul,0,0)
        obojeWrite(sCel,0,0,0,sCel,0,0,0)
        obojeWrite(spodniPul,0,0,0,spodniPul,0,0,0)
        print("Změna oboje: Zavírání")

    elif garaz == 50 and brana == 500:
        obojeWrite(spodniPul,0,0,0,0,0,0,horniPul)
        obojeWrite(sCel,0,0,0,0,0,0,sCel)
        obojeWrite(horniPul,spodniPul,0,0,0,0,horniPul,spodniPul)
        obojeWrite(0,sCel,0,0,0,0,sCel,0)
        obojeWrite(0,horniPul,spodniPul,0,0,horniPul,spodniPul,0)
        obojeWrite(0,0,sCel,0,0,sCel,0,0)
        obojeWrite(0,0,horniPul,spodniPul,horniPul,spodniPul,0,0)
        obojeWrite(0,0,0,sCel,sCel,0,0,0)
        obojeWrite(0,0,0,horniPul,spodniPul,0,0,0)
        print("Garáž otevírání, brána zavírání")

    elif garaz == 500 and brana == 50:
        obojeWrite(0,0,0,horniPul,spodniPul,0,0,0)
        obojeWrite(0,0,0,sCel,sCel,0,0,0)
        obojeWrite(0,0,horniPul,spodniPul,horniPul,spodniPul,0,0)
        obojeWrite(0,0,sCel,0,0,sCel,0,0)
        obojeWrite(0,horniPul,spodniPul,0,0,horniPul,spodniPul,0)
        obojeWrite(0,sCel,0,0,0,0,sCel,0)
        obojeWrite(horniPul,spodniPul,0,0,0,0,horniPul,spodniPul)
        obojeWrite(sCel,0,0,0,0,0,0,sCel)
        obojeWrite(spodniPul,0,0,0,0,0,0,horniPul)
        print("Garáž zavírání, brána otevírání")

    else:
        print("Neznámý stav: "+str(hodnota))
    obojeReset()

def checkState():
    garaz, brana = stateReadDisplay()
    print('Garaz'+str(garaz))
    print('Brana'+str(brana))
    if  garaz+brana > 49:
        writeState(garaz,brana)


#while True:
 #   checkState()
 #   sleep(2)

if __name__=='__main__':
    checkState()