from flask import Flask, render_template, jsonify
from garageOpen import garageSwitch
from stateIO import stateReset,stateRead,stateReadJSON
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


app = Flask(__name__)

@app.route('/')
def index():
    return stateRead()

@app.route('/garageOpen')
def garageOpen():
    garageSwitch()
    return stateRead()

@app.route('/json')
def postJson():
    gar, gat = stateReadJSON()
    return jsonify(
        garage=gar,
        gate=gat
    )


@app.route('/resetState/<int:gar>/<int:gat>')
def resetState(gar,gat):
    stateReset(gar,gat)
    return stateRead()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

   