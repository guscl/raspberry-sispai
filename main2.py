#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import request_maker as server

#Outputs
buzzerNobody = 29
buzzerSomeone = 31
engineOpening = 33
engineClosing = 35
pump = 37


#Inputs
openedSensor = 3
closedSensor = 5
crashSensor = 7
xbeeButton = 11
start = 13
infraRed = 15

GPIO.cleanup()

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
	print "idle()"
	print GPIO.input(start) ," ", GPIO.input(xbeeButton)
	GPIO.output(buzzerSomeone, 0)
	GPIO.output(buzzerNobody, 0)
	if GPIO.input(infraRed):
		print "manda info pro site"

	if GPIO.input(start) and GPIO.input(xbeeButton):
		time.sleep(1)					
		GPIO.output(pump, 0)
		GPIO.output(engineOpening, 1)
		print "engineOpening ON"
		while True:
			#print GPIO.input(openedSensor)
			if GPIO.input(xbeeButton) == False:
				time.sleep(0.1)	
				if GPIO.input(infraRed):
					time.sleep(0.1)	
					GPIO.output(buzzerSomeone, 1)
					GPIO.output(buzzerNobody, 0)
					server.messageServer("fall")
					print "buzzerSomeone ON"
				else:
					GPIO.output(buzzerNobody, 1)
					GPIO.output(buzzerSomeone, 0)
					print "buzzerNobody ON"

			if GPIO.input(xbeeButton) == True:
				print "o cara ta na area ABRINDO"
				#print GPIO.output(engineOpening)
				server.messageServer("getin")
				GPIO.output(buzzerSomeone, 0)
				GPIO.output(buzzerNobody, 0)
				if GPIO.input(openedSensor) == False:
					time.sleep(0.3)
					GPIO.output(engineOpening, 0)
					GPIO.output(buzzerSomeone, 0)
					GPIO.output(buzzerNobody, 0)
					print "ABRIU"
					postOpening()
					break
				
			if GPIO.input(openedSensor) == False:
				time.sleep(0.3)
				GPIO.output(engineOpening, 0)
				GPIO.output(buzzerSomeone, 0)
				GPIO.output(buzzerNobody, 0)
				print "ABRIU"
				server.messageServer("open")
				postOpening()
				break

def forcedOpen():
	print "forcedOpen()"
	GPIO.output(pump, 0)
	GPIO.output(engineOpening, 1)
	while True:
		if GPIO.input(openedSensor) == False:
			GPIO.output(engineOpening, 0)
			GPIO.output(buzzerSomeone, 0)
			GPIO.output(buzzerNobody, 0)
			postOpening()
			break	

#tem que por while na main
def postOpening():
	print "postOpening()"
	while True:
		if not GPIO.input(xbeeButton):
			time.sleep(0.1)	
			if GPIO.input(infraRed):
				time.sleep(0.1)	
				print "SAIU MAS TEM ALGUEM"
				server.messageServer("getout")
				GPIO.output(buzzerSomeone, 1)
				time.sleep(0.5)	
				GPIO.output(buzzerSomeone, 0)
				time.sleep(0.5)
			else:
				time.sleep(1)
				closing()

		if GPIO.input(xbeeButton):
			time.sleep(0.1)	
			print "USANDO A PISCINA"
			GPIO.output(buzzerSomeone, 0)

def closing():
	print "closing()"
	GPIO.output(engineClosing, 1)
	print GPIO.input(crashSensor) ," ", GPIO.input(infraRed)
	while True:
		if not GPIO.input(crashSensor) or GPIO.input(infraRed):
			time.sleep(0.1)	
			#Someone has fallen
			GPIO.output(buzzerSomeone, 1)
			GPIO.output(engineClosing, 0)
			print "CAIU ALGUEM"	
			server.messageServer("fall")	
			forcedOpen()
			break
		if GPIO.input(closedSensor) == False:
			print "FECHOU"
			server.messageServer("close")
			GPIO.output(engineClosing, 0)
			GPIO.output(pump, 1)
			waiting()
			break


def waiting():
	print "waiting"
	while True:
		time.sleep(0.1)	
		opening()
		

if __name__ == '__main__':
	waiting()	
	GPIO.cleanup()
	
		
			
			
	

		
		
		










	
