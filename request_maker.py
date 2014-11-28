import RPi.GPIO as GPIO
import time
import httplib


httpServ = httplib.HTTPConnection("10.42.0.1", 8000)
httpServ.connect()


def eventHandler (pin):
    print "handling button event"
    httpServ.request('GET', '/core/sensors/', '')

    GPIO.output(7,False)
    GPIO.output(7,True)
    time.sleep(2)
    # turn the green LED off
    GPIO.output(7,False)

def messageServer(message):
	print "Mandei a requisição" + message 
    httpServ.request('GET', message, 'root')


def deventHandler (pin):
    print "handling button event"

    GPIO.output(7,False)
    GPIO.output(7,True)

    time.sleep(2)

    # turn the green LED off
    GPIO.output(7,False)
