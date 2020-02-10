import serial
from time import sleep
import os

os.system('bash upload_arduino_code.sh')	#uploads arduino code rather than executing it separately

#define the serial communication between the arduino and pi

with serial.Serial('/dev/ttyACM0', 9600) as arduino:

	#waits for arduino before executing any code

	ready = arduino.read(5)
	print('ready')



	value = input('Enter a value (65 will return the value  A): ')

	#loops the program so value will constantly be written

	while True:
		arduino.write(bytearray([value]))		#writes the inputted value to the arduino
		response = arduino.read()			#reads the return value from arduino and prints
		print(response)
		sleep(1)
