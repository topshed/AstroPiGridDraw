import os, sys

mypath = os.path.dirname(os.path.abspath(__file__))
if os.path.isfile("/proc/device-tree/hat/product"):
	file = open("/proc/device-tree/hat/product","r")
	hat = file.readline()
	if  hat == "Sense HAT\x00":
		print('Sense HAT detected')
		file.close()
		os.system("/usr/bin/env python3 " + mypath+"/8x8grid-sense.py")
	elif hat == "Unicorn HAT\x00":
		print('Unicorn HAT detected')
		file.close()
		os.system("/usr/bin/env python3 " + mypath+"/8x8grid-unicorn.py")
else:
	print("Unknown HAT : " + " Setup for sense_emu")
	os.system("/usr/bin/env python3 " + mypath+"/8x8grid-no-sense_emu.py")

