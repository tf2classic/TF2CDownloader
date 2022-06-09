from platform import system

keepzip = False

if system() == 'Windows':
	TEMP_PATH = ".temp/"
else:
	TEMP_PATH = "/tmp/tf2cdownloader/"
	
ARIA2C_BINARY = None
TAR_BINARY = None
# ZSTD_BINARY is only used on Linux.
ZSTD_BINARY = None
SOURCEMODS_PATH = None
MAKE_SYMLINK = False
MOVE_TF2CLASSIC_FOLDER = False
DEFAULT_SOURCEMODS_PATH = None
