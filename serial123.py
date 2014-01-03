#!/usr/bin/python
import serial
import os
from serial.serialutil import SerialException

ser = serial.Serial('/dev/ttyACM0')
print ser.portstr
ser.baudrate=9600
ser.write("s")
try:
	while(1):
	
		try:
			v=ser.read(20)
		except SerialException:
			os.system('gnome-screensaver-command -l')
			continue
		except ValueError:
			os.system('gnome-screensaver-command -l')
			continue
		try:
			v = int(v)
		except ValueError:
			os.system('gnome-screensaver-command -l')
			continue
		if int(v)<11111111111111111111:
			print 'out'
			os.system('gnome-screensaver-command -l')
		else:
			print 'in'
except KeyboardInterrupt:
	print 'close';
		

ser.close()
