#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

def gpioSwitch(obj):
    if(obj == "garage"):
        relay = 27
    if(obj == "gate"):
        relay = 22

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay, GPIO.OUT)
    for i in range(1):
        GPIO.setup(relay, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.setup(relay, GPIO.LOW)
        time.sleep(0.2)

    GPIO.cleanup(relay)



    