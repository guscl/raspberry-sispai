import RPi.GPIO as GPIO
import time
import httplib


def deventHandler (pin):
    print "handling button event"

    GPIO.output(7,False)
    GPIO.output(7,True)

    time.sleep(2)

    # turn the green LED off
    GPIO.output(7,False)

def eventHandler (pin):
    print "handling button event"
    httpServ = httplib.HTTPConnection("10.42.0.1", 8000)
    httpServ.connect()
    httpServ.request('GET', '/core/sensors/', '')

    GPIO.output(7,False)
    GPIO.output(7,True)
    time.sleep(2)
    # turn the green LED off
    GPIO.output(7,False)
