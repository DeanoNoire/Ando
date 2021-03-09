from flask import Flask, render_template
from garageOpen import garageSwitch
from stateIO import stateReset,stateRead
import RPi.GPIO as GPIO
import time

garageRelay = 27
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route('/')
def index():
    return stateRead()

@app.route('/garageOpen')
def garageOpen():
    garageSwitch()
    return stateRead()

@app.route('/resetState/<int:gar>/<int:gat>')
def resetState(gar,gat):
    stateReset(gar,gat)
    return stateRead()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')