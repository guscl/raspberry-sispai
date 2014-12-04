#!/usr/bin/python
from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

#Initial setUp
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, False)
now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")

#Defining how the program will answers to requests 

@app.route("/40/on")
def action4on():
	print "Turn On"
	GPIO.output(40, True)	
	message = "GPIO 40 was turned on"
	templateData = {
		'message' : message,
		'time' : timeString
    }
	return render_template('gpioweb.html', **templateData)
    
@app.route("/40/off")
def action4off():
	print "Turn Off"
	GPIO.output(40, False)
	message = "GPIO 40 was turned off."
	templateData = {
		'message' : message,
		'time' : timeString
	}
	return render_template('gpioweb.html', **templateData)

if __name__ == "__main__":
     app.run(threaded=True,host="192.168.1.32")
  
