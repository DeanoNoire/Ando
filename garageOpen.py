#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
from stateIO import stateRead,stateChange

def garageSwitch():
    switch = 27

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switch, GPIO.OUT)

    for i in range(1):
        GPIO.setup(switch, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.setup(switch, GPIO.LOW)
        time.sleep(0.2)

    GPIO.cleanup()

    stateChange('garage')

    