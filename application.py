from flask import Flask, render_template, jsonify,redirect, request
import garageOpen
from stateIO import stateReset,stateRead,stateReadJSON
import RPi.GPIO as GPIO

pwd = '2591107373647'

GPIO.setmode(GPIO.BCM)


app = Flask(__name__)

@app.route('/')
def index():
    gar, gat = stateReadJSON()
    garStr = 'gar'+str(gar)
    gatStr = 'gat'+str(gat)
    return render_template('index.html',garage=garStr,gate=gatStr)

@app.route('/garageOpen', methods = ['POST'])
def garageOpenFun():
        msg = request.form['msg']
        print('MSG: ',msg)
        if(msg == pwd):
            garageOpen.garageSwitch()
            return redirect('/')
        else: 
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
    app.run(host='0.0.0.0')
    #app.run(host='0.0.0.0',ssl_context="adhoc")
    #app.run(host='0.0.0.0',ssl_context=('cert.pem','key.pem'))

   