import os
import shutil
import sys
if os.name == 'nt':
	import winreg

import vars
import gui

registry = 0
registry_key = 0

# get sourcemods directory from registry
def sourcemods_path():
	if os.name == 'nt':
		try:
			global registry
			global registry_key
			if registry == 0:
				registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
				registry_key = winreg.OpenKeyEx(registry, "SOFTWARE\Valve\Steam", access=winreg.KEY_ALL_ACCESS)
			
			value = winreg.QueryValueEx(registry_key, "SourceModInstallPath")
			return value[0]
		except Exception:
			return None
def set_sourcemods_path(path):
	if os.name == 'nt':
		global registry
		global registry_key
		if registry == 0:
			registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
			registry_key = winreg.OpenKeyEx(registry, "SOFTWARE\Valve\Steam")
		
		value = winreg.SetValue(registry_key, "SourceModInstallPath", winreg.REG_SZ, path)

def setup_path():
	confirm = False
	vars.SOURCEMODS_PATH = sourcemods_path()
	steamfound = isinstance(vars.SOURCEMODS_PATH, str)
	if steamfound:
		gui.message_quick("Sourcemods folder was automatically found at: " + vars.SOURCEMODS_PATH)
		if gui.message_yes_no("It's the recommended installation location. Would you like to install TF2Classic there?"):
			vars.TF2C_PATH = os.path.join(vars.SOURCEMODS_PATH, "tf2classic")
			confirm = True
		else:
			# check if any sourcemods exists there
			no_sourcemods = True
			for file in os.listdir(vars.SOURCEMODS_PATH):
				if os.path.isdir(file):
					no_sourcemods = False
			
			if no_sourcemods:
				if gui.message_yes_no("Then, would you like to move the sourcemods folder location?"):
					gui.message_quick("Please enter the location of the new sourcemods folder.")
					vars.SOURCEMODS_PATH = gui.message_dir("sourcemods")
					set_sourcemods_path(vars.SOURCEMODS_PATH)
					vars.TF2C_PATH = os.path.join(vars.SOURCEMODS_PATH, "tf2classic")
				else:
					gui.message_quick("Then, enter the location in which TF2Classic will be installed to. NOTE: Steam will not be able to find it!")
					vars.TF2C_PATH = os.path.join(gui.message_dir("location"), "tf2classic")
	else:
		gui.message_quick("WARNING: Steam has not been found.")
		if os.name == 'nt':
			vars.SOURCEMODS_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\sourcemods"
		else:
			vars.SOURCEMODS_PATH = "~/.steam/steam/steamapps/sourcemods/"
		gui.message_quick("The recommended installation location would be " + vars.SOURCEMODS_PATH + ".")
		if gui.message_yes_no("Would you like to install TF2Classic there?"):
			vars.TF2C_PATH = os.path.join(vars.SOURCEMODS_PATH, "tf2classic")
			confirm = True
		else:
			gui.message_quick("Then, enter the location in which TF2Classic will be installed to.")
			vars.TF2C_PATH = os.path.join(gui.message_dir("location"), "tf2classic")
		
	if not confirm:
		if not gui.message_yes_no("TF2Classic will be installed in " + vars.TF2C_PATH + "\nDo you accept?"):
			print("Resetting...\n")
			setup_path()

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