import  RPi.GPIO as GPIO
import time
import garageOpen

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

bounce = 10000

def button_handler(pin):
    print("Button press 1")
    

def button_handlerTwo(pin):
    print("Button press 2")
    garageOpen.garageSwitch()

GPIO.add_event_detect(16, GPIO.RISING,callback=button_handler, bouncetime=bounce)
GPIO.add_event_detect(26, GPIO.RISING,callback=button_handlerTwo, bouncetime=bounce)

while True:
    time.sleep(1)
       
