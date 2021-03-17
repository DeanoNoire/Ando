#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
from stateIO import stateRead,stateChange

def garageSwitch():
    GPIO.setmode(GPIO.BCM)
    garageRelay = 27
    GPIO.setup(garageRelay, GPIO.OUT)
    for i in range(1):
        GPIO.setup(garageRelay, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.setup(garageRelay, GPIO.LOW)
        time.sleep(0.2)

    GPIO.cleanup(garageRelay)
    stateChange('garage')
    
    

    