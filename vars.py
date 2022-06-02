import os

keepzip = False

if os.name == 'nt':
	TEMP_PATH = ".temp/"
else:
	TEMP_PATH = "/var/tmp/tf2cdownloader/"
	
ARIA2C_BINARY = None
SEVENZ_BINARY = None