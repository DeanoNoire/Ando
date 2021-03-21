import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def button_handler(pin):
    print("Button press 1")

def button_handlerTwo(pin):
    print("Button press 2")

GPIO.add_event_detect(16, GPIO.RISING,callback=button_handler, bouncetime=500)
GPIO.add_event_detect(26, GPIO.RISING,callback=button_handlerTwo, bouncetime=500)

while True:
    time.sleep(1)
       
