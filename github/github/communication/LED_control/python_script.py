import serial
import os
from time import sleep

os.system('bash upload_arduino_code.sh')	#uploads arduino code

with serial.Serial('/dev/ttyACM0', 9600) as arduino:	#defining communication between pi and arduino

	#waits for arduino before executing further code

	ready = arduino.read(5)
	print("ready")

	while True:
		arduino.write(bytearray([1]))
		response = arduino.read()
		print("LED is blinking")
