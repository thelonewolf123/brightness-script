#!/usr/bin/python3

import sys
import subprocess

graphics = subprocess.check_output(['ls','/sys/class/backlight/']).decode('utf-8')[:-1]
file = open(f'/sys/class/backlight/{graphics}/brightness', 'r+') 

brightness=0

if len(sys.argv) == 2:
	
	if int(sys.argv[1]) <= 100 and int(sys.argv[1]) >0:
		brightness=(int(sys.argv[1]))*2.55
		
		for each in file: 
		    brightness=int(each)

		brightness=int((int(sys.argv[1]))*2.55)
		file.write(str(brightness))
		print(f"Brightness has been successfully changed to {sys.argv[1]}%")
		file.close() 
	
	else:
		print("Invalid brightness value, please Enter the value between 1 to 100.")

else:
	print(f"Usage: {sys.argv[0]} <brightness in % >")
	