import firebase_admin
from firebase_admin import credentials, firestore
import RPi.GPIO as GPIO
import sys

try:
	creds = credentials.Certificate("ieeeworkshopiot.json")
	firebase = firebase_admin.initialize_app(creds)
	db = firestore.client()
	print("Google Firebase is connected successfully!")
except:
	print("Connection Error!")
	sys.exit()

led = db.collection(u'led').document(u'led1')

GPIO.setmode(GPIO.BCM)				# set connection mode to be BCM
led_pin = 4							# assign BCM4 to led output

GPIO.setup(led_pin, GPIO.OUT)		# set LED pin to be output pin
GPIO.output(led_pin, 0)				# initialize LED to LOW
print("LED control system initialized!")

while True:
	try:
		if led.get().to_dict()['state']:		# check LED state on Firebase
			GPIO.output(led_pin, 1)	# if True, set LED to HIGH
			print("LED turned on!")
		else:
			GPIO.output(led_pin, 0)	# otherwise, set LED to LOW
			print("LED turned off!")
	except KeyboardInterrupt:		# when ctrl-C pressed
		break						# break out of the loop

print("LED control system terminated!")
GPIO.cleanup()
	


