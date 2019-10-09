import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red_light = 2
yellow_light = 3
green_light = 4

GPIO.setup(red_light,GPIO.OUT)
GPIO.setup(yellow_light,GPIO.OUT)
GPIO.setup(green_light,GPIO.OUT)

GPIO.output(red_light , GPIO.LOW)
GPIO.output(yellow_light , GPIO.LOW)
GPIO.output(green_light , GPIO.LOW)

try:
	while True:
		GPIO.output(red_light , GPIO.HIGH)
		time.sleep(5)
		GPIO.output(green_light , GPIO.HIGH)
		GPIO.output(red_light , GPIO.LOW)
		time.sleep(5)
		GPIO.output(green_light , GPIO.LOW)
		GPIO.output(yellow_light , GPIO.HIGH)
		time.sleep(1)
		GPIO.output(yellow_light , GPIO.LOW)
except KeyboardInterrupt:
	GPIO.cleanup()
