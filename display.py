import tm1637
from time import sleep
import json

tm = tm1637.TM1637(clk=21,dio=20)

tm.brightness(val=2)

sleepTime = 0.3
loops = 5
hodnota = 0

s100 = 0b00000001
s110 = 0b01000001
s111 = 0b01001001
s011 = 0b01001000
s001 = 0b00001000

def stateReadDisplay():
    json_file = open('states.json','r')
    data = json.load(json_file)
    return data['garage']+(data['gate']*2)
    
def writeState(hodnota):
    if 50 <= hodnota <= 51:
        tm.write([s100,s100,0,0])
        sleep(sleepTime)
        tm.write([s110,s110,0,0])
        sleep(sleepTime)
        tm.write([s111,s111,0,0])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna garáž: Otevírání - "+str(hodnota))

    elif 100 <= hodnota <= 101:
        tm.write([0,0,s100,s100])
        sleep(sleepTime)
        tm.write([0,0,s110,s110])
        sleep(sleepTime)
        tm.write([0,0,s111,s111])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna brána: Otevírání - "+str(hodnota))

    elif 500 <= hodnota <= 501:
        tm.write([s001,s001,0,0])
        sleep(sleepTime)
        tm.write([s011,s011,0,0])
        sleep(sleepTime)
        tm.write([s111,s111,0,0])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna garáž: Zavírání - "+str(hodnota))

    elif 1000 <= hodnota <= 1001:
        tm.write([0,0,s001,s001])
        sleep(sleepTime)
        tm.write([0,0,s011,s011])
        sleep(sleepTime)
        tm.write([0,0],s111,s111)
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna brána: Zavírání"+str(hodnota))

    elif hodnota == 600:
        tm.write([s001,s001,s100,s100])
        sleep(sleepTime)
        tm.write([s011,s011,s110,s110])
        sleep(sleepTime)
        tm.write([s111,s111,s111,s111])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna oboje: garage close / brána open "+str(hodnota))

    elif hodnota == 1050:
        tm.write([s100,s100,s001,s001])
        sleep(sleepTime)
        tm.write([s110,s110,s011,s011])
        sleep(sleepTime)
        tm.write([s111,s111,s111,s111])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna oboje: garage open / brána close "+str(hodnota))

    elif hodnota == 150:
        tm.write([s100,s100,s100,s100])
        sleep(sleepTime)
        tm.write([s110,s110,s110,s110])
        sleep(sleepTime)
        tm.write([s111,s111,s111,s111])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna oboje: open "+str(hodnota))

    elif hodnota == 1500:
        tm.write([s001,s001,s001,s001])
        sleep(sleepTime)
        tm.write([s011,s011,s011,s011])
        sleep(sleepTime)
        tm.write([s111,s111,s111,s111])
        sleep(sleepTime)
        tm.write([0,0,0,0])
        #print("Změna oboje: close "+str(hodnota))

    else:
        print("Neznámý stav: "+str(hodnota))


def checkState():
    hodnota = stateReadDisplay()
    if  hodnota > 49:
        writeState(hodnota)

while True:
    checkState()
    sleep(2)
