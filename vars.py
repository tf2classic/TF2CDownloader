from platform import system

keepzip = False

OS_TYPE = system()
if OS_TYPE() == 'Windows':
	TEMP_PATH = ".temp/"
else:
	TEMP_PATH = "/var/tmp/tf2cdownloader/"
	
ARIA2C_BINARY = None
SEVENZ_BINARY = None

SOURCEMODS_PATH = None
TF2C_PATH = None