from flask import Flask, render_template
from garageOpen import garageSwitch
import RPi.GPIO as GPIO
import time

garageRelay = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(garageRelay, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/garageOpen')
def garageOpen():
    garageSwitch()
    return 'Garage open'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')