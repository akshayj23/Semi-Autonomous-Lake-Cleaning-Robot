from flask import Flask
from flask import Markup, flash, session
from flask import render_template, request,jsonify
import numpy as np
import time
import serial
#For learning Flask must follow the link-https://projects.raspberrypi.org/en/projects/python-web-server-with-flask

#ser=serial.Serial('/dev/ttyACM0',baudrate=115200)
# Create the server
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/right_side')
#Below function runs when /right_side is called by the client
def onright():
    #Sending r on the serial to arduino
    ser.write('r')
    print("right")
    #Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp
@app.route('/left_side')
def onleft():
    # Sending l on the serial to arduino
    ser.write('l')
    print("left")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp
@app.route('/up_side')
def onup():
    ser.write('f')
    # Sending f on the serial to arduino
    print("up")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp
@app.route('/down_side')
def ondown():
    ser.write('b')
    # Sending b on the serial to arduino
    print("down")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp
@app.route('/stop')
def onstop():
    # Sending s on the serial to arduino
    ser.write('s')
    print("stop")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp
@app.route('/unload')
def unload():
    ser.write('u')
    # sending u to unload
    print("unload")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp

@app.route('/con-on')
def con():
    ser.write('c')
    #sending c to make the conveyor on
    print("conveyor on")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp

@app.route('/con-off')
def coff():
    ser.write('o')
    # sending o to make the conveyor off
    print("conveyor off")
    # Creating response packet returning it to the client
    resp = jsonify(success=True)
    return resp

@app.route("/")
#Default path set to load html file
def onload():
    from neo6 import GpsNeo6
    gps=GpsNeo6(port="/dev/ttyAMA0",debit=9600,diff=2)
    while True:
        gps.traite()
        print(gps) # print all info
        latstr=str(gps.latitude)
        lonstr=str(gps.longitude)
        x="Latitude=" + latstr + " Longitude=" + lonstr
	y="250g"
        print(gps.latitude,gps.longitude)
        print(latstr,lonstr)
        message=Markup(x)
        message2 = Markup(y)
        message3 = Markup(x)
        message4 = Markup(x)
        flash(message)
        #flash(message2)
        #flash(message3)
        #flash(message4)
        return render_template('main.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
