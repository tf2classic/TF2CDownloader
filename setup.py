import os
import shutil
import sys

import vars
import gui

def setup_binaries():
	if os.name == 'nt':
		vars.ARIA2C_BINARY = sys._MEIPASS + "/aria2c.exe"
		vars.SEVENZ_BINARY = sys._MEIPASS + "/7za.exe"
	else:
		if shutil.which("aria2c") is None:
			gui.message_end("You need to install Aria2 to use this script.", 1)
		else:
			vars.ARIA2C_BINARY = "aria2c"

		if shutil.which("7zz") is None and shutil.which("7z") is None:
			gui.message_end("You need to install 7-Zip or p7zip to use this script.", 1)
		elif shutil.which("7zz") is not None:
			vars.SEVENZ_BINARY = "7zz"
		else:
			vars.SEVENZ_BINARY = "7z"