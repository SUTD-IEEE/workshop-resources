import RPi.GPIO as GPIO  # import GPIO Python library
import time				 # import time library to set delay and stopwatch

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
	duration = end_time - start_time
	distance = duration * 34300 / 2	    # distance calculation in cm
	distance = round(distance, 2)
	return distance

# entering distance measuring loop
try:
	while True:

		distance = measure_cm()			# return measured distance
		print("Current distance: {} cm".format(distance))
		if distance < CRASH_DISTANCE:
			print("DANGER")
		else:
			print("SAFE")

		time.sleep(0.1)

except KeyboardInterrupt:
	print("Measurement Terminated!")
	GPIO.cleanup()						# this is IMPORTANT!
