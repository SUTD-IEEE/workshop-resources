import firebase_admin
from firebase_admin import credentials, firestore

import RPi.GPIO as GPIO  # import GPIO Python library
import time				 # import time library to set delay and stopwatch

creds = credentials.Certificate("{Your credential.json filename here}")
app = firebase_admin.initialize_app(creds)
db = firestore.client()	 # initialize firestore database
myDocument = db.collection(u'ultrasonic').document(u'myDevice')

GPIO.setmode(GPIO.BCM)   # we set GPIO mode to be BCM
						 # so later we match BCM pin number
						 # instead of GPIO pin number

TRIG = 23  				 # GPIO Pin 16 which is BCM 23
ECHO = 24  				 # GPIO Pin 18 which is BCM 24
CRASH_DISTANCE = 10		 # in cm

print("Initialize Distance Measurement...")

GPIO.setup(TRIG, GPIO.OUT)  # set TRIG to be output pin
GPIO.setup(ECHO, GPIO.IN)   # set ECHO to be input pin

GPIO.output(TRIG, 0)		# TRIG do not emit ultrasound

time.sleep(2) 				# some delay for hardware to initialize

# let's define a measurement function
def measure_cm():
	GPIO.output(TRIG, 1)				# send a pulse
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)				# stop sending a pulse
	while GPIO.input(ECHO) == 0:	    # set start timestamp when not
		start_time = time.time()		# receive any signal
	while GPIO.input(ECHO) == 1:		# set end timestamp when
		end_time = time.time()			# receive a pulse signal
	if end_time and start_time:
		duration = end_time - start_time
	else:
		return None
	distance = duration * 34300 / 2	    # distance calculation in cm
	distance = round(distance, 2)
	return distance

# entering distance measuring loop
try:
	while True:

		distance = measure_cm()			# return measured distance
		if distance is None:
			break
		print("Current distance: {} cm".format(distance))
		if distance < CRASH_DISTANCE:
			print("DANGER")
			myDocument.update(			# update value in database based on key
			{
				"isDanger": True
			}
			)
		else:
			print("SAFE")
			myDocument.update(
			{
				"isDanger": False
			}
			)

		time.sleep(0.1)

except KeyboardInterrupt:
	print("Measurement Terminated!")
	GPIO.cleanup()						# this is IMPORTANT!
