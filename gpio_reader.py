#!/usr/bin/env python

import RPi.GPIO as GPIO 
from time import sleep
from garageOpen import garageSwitch
 
def detected(channel):
    print("Stisknuto: "+str(channel))
    switcher = {
            14: lambda: garageSwitch(),
            15: lambda: gateSwitch(),
            18: lambda: zatimNenastaveno(),
            23: lambda: zatimNenastaveno()
        } 
    func = switcher.get(channel, lambda: 'Neplatný')
    print(func())
 
def doNothing():
    sleep(0.1)

def gateSwitch():
    print('Switchuju branu')

def zatimNenastaveno():
    print('Zatím nenakonfigurované tlačítko')

INPUT_A = 14
INPUT_B = 15  
INPUT_C = 18 
INPUT_D = 23  
bouncetimeVal = 2000
GPIO.setmode(GPIO.BCM) 
GPIO.setup(INPUT_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_D, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

GPIO.add_event_detect(INPUT_A,GPIO.FALLING,callback=detected,bouncetime=bouncetimeVal)
GPIO.add_event_detect(INPUT_B,GPIO.FALLING,callback=detected,bouncetime=bouncetimeVal)
GPIO.add_event_detect(INPUT_C,GPIO.FALLING,callback=detected,bouncetime=bouncetimeVal)
GPIO.add_event_detect(INPUT_D,GPIO.FALLING,callback=detected,bouncetime=bouncetimeVal)

while True:
    doNothing()



    


