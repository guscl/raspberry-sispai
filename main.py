#!/usr/bin/python

import time
import RPi.GPIO as GPIO

#Outputs
buzzerNobody = 26
buzzerSomeone = 19
engineOpening = 22
engineClosing = 24
pump = 23


#Inputs
xbeeButton = 8
openedSensor = 3
closedSensor = 5
crashSensor = 7
infraRed = 12
start = 10


#GPIO setUp
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzerNobody, GPIO.OUT)
GPIO.setup(buzzerSomeone, GPIO.OUT)
GPIO.setup(engineOpening, GPIO.OUT)
GPIO.setup(engineClosing, GPIO.OUT)
GPIO.setup(pump, GPIO.OUT)
GPIO.setup(xbeeButton, GPIO.IN)
GPIO.setup(openedSensor, GPIO.IN)
GPIO.setup(closedSensor, GPIO.IN)
GPIO.setup(crashSensor, GPIO.IN)
GPIO.setup(infraRed, GPIO.IN)
GPIO.setup(start, GPIO.IN)

GPIO.output(buzzerNobody, False)
GPIO.output(buzzerSomeone, False)
GPIO.output(engineOpening, False)
GPIO.output(engineClosing, False)
GPIO.output(pump, False)

def opening():
	if GPIO.input(start) and GPIO.input(xbeeButton):				
		GPIO.output(pump, 0)
		GPIO.output(engineOpening, 1)
		while True:
			if GPIO.input(xbeeButton) == False:
				if GPIO.input(infraRed):
					GPIO.output(buzzerSomeone, 1)
				else:
					GPIO.output(buzzerNobody, 1)
			if GPIO.input(closedSensor):
				GPIO.output(engineOpening, 0)
				GPIO.output(buzzerSomeone, 0)
				GPIO.output(buzzerNobody, 0)
				postOpening()
				break

def forcedOpen():				
	GPIO.output(pump, 0)
	GPIO.output(engineOpening, 1)
	while True:
		if GPIO.input(closedSensor):
			GPIO.output(engineOpening, 0)
			GPIO.output(buzzerSomeone, 0)
			GPIO.output(buzzerNobody, 0)
			postOpening()
			break	

#tem que por while na main
def postOpening():
	if not GPIO.input(xbeeButton):
		if GPIO.input(infRared):
			GPIO.output(buzzerSomeone, 1)
		else:
			time.sleep(10)
			closing()

def closing():
	GPIO.output(engineClosing, 1)
	while True:
		if GPIO.input(crashSensor) or GPIO.input(infraRed):
			#Someone has fallen
			GPIO.output(buzzerSomeone, 1)
			GPIO.output(engineClosing, 0)
			forecedOpen()
			break
		if GPIO.input(closedSensor):
			GPIO.output(engineClosing, 1)
			GPIO.output(pump, 1)
			opening()

if __name__ == '__main__':
	opening()
	GPIO.cleanup()
	
		
			
			
	

		
		
		










	
