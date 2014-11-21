#!/usr/bin/env python

from flask import Flask, render_template
import time
import RPi.GPIO as GPIO
import datetime
app = Flask(__name__)


    GPIO.setmode(GPIO.BCM)
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")

    # setup pin 23 to stream data
    GPIO.setup(23,GPIO.IN)
    # setup pin 24 and 25 to receive data
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

    #This pin will receive data from the web
    GPIO.setup(4, GPIO.OUT)


    GPIO.output(25,True)

    while True:
        if GPIO.input(23):
             GPIO.output(25,False)
             print "button true"
        else:
             GPIO.output(24,False)
             GPIO.output(25,True)
             print "button false"

        time.sleep(0.1)

   

    GPIO.cleanup()

@app.route("/")
def hello():
   templateData = {
      'title' : 'RPi GPIO Control',
      'time': timeString
      }
   return render_template('gpioweb.html', **templateData)

if __name__=="__main__":
    main()

