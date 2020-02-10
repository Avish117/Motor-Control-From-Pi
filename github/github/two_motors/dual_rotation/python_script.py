import serial
import os
from time import sleep

os.system('bash upload_arduino_code.sh')

serial.Serial('/dev/ttyACM0', 9600) = arduino1
serial.Serial('/dev/ttyACM2', 9600) = arduino2

ready = arduino1.read()
print("Arduino 1 is ready")
ready = arduino2.read()
print("Arduino 2 is ready")

with arduino1 and arduino2:
	value = input("Enter a number: ")
	arduino1.write(value)
	arduino2.write(value)
	response1 = arduino1.read()
	print("Arduino 1 good")
	
