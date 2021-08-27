import garageOpen
from stateIO import stateReset,stateRead,stateReadJSON
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)



def garageOpenFun():
    garageOpen.garageSwitch()
    return stateRead()


if __name__ == '__main__':
    garageOpenFun()
