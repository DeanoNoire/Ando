import  RPi.GPIO as GPIO
import time
import stateIO

bounce = 10000

def buttonSetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)



def button_handler(pin):
    print("Changing Garage - Button press 1")
    stateIO.stateChange("garage")
    

def button_handlerTwo(pin):
    print("Changing Gate - Button press 2")
    stateIO.stateChange("gate")

def waitButton():
        GPIO.add_event_detect(16, GPIO.RISING,callback=button_handler, bouncetime=bounce)
        GPIO.add_event_detect(26, GPIO.RISING,callback=button_handlerTwo, bouncetime=bounce)


       
if __name__ == "__main__":
    waitButton()