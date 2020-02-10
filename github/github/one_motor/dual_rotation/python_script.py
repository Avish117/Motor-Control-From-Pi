import serial
import os
from time import sleep

os.system('bash upload_arduino_code.sh')

with serial.Serial('/dev/ttyACM0', 9600) as arduino:
	response = arduino.read(5)
	print("ready")

	value = input('Enter a number between 0 and 200: ')

	while True:
		arduino.write(bytearray([value]))
		response = arduino.read()
		print("Arduino has received value")
		sleep(1)
