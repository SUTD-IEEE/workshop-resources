import serial
from time import sleep
import sys

ser = serial.Serial('/dev/ttyUSB0',9600)

try:
	while True:
		x = input("Display number? : ")
		x += '\n'
		ser.write(str.encode(x))
		sleep(0.1)
finally:
	ser.close()
	print("")
	sys.exit()
