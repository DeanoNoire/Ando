from flask import Flask, render_template, jsonify,redirect
import garageOpen
from stateIO import stateReset,stateRead,stateReadJSON
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)


app = Flask(__name__)

@app.route('/')
def index():
    gar, gat = stateReadJSON()
    garStr = 'gar'+str(gar)
    gatStr = 'gat'+str(gat)
    return render_template('index.html',garage=garStr,gate=gatStr)

@app.route('/garageOpen')
def garageOpenFun():
    garageOpen.garageSwitch()
    #return stateRead()
    return redirect('/')

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
    app.run(host='0.0.0.0', port=5000)

   