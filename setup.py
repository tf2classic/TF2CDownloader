from os import path as os_path
from shutil import which
from sys import _MEIPASS as MEIPASS
if OS_TYPE == 'Windows':
	import winreg
import vars
import gui

registry = 0
registry_key = 0

def sourcemods_path():
	"""
	Find path to sourcemod folder.
	"""
	if OS_TYPE == 'Windows':
		try:
			global registry
			global registry_key
			if registry == 0:
				registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
				registry_key = winreg.OpenKeyEx(registry, 'SOFTWARE\Valve\Steam', access=winreg.KEY_ALL_ACCESS)
			
			value = winreg.QueryValueEx(registry_key, 'SourceModInstallPath')
			return value[0]
		except Exception:
			return None
	else:
		try:
			linux_dirs = {
				'~/.steam/steam/steamapps/sourcemods/',
				# these locations are mentioned in old posts on forums, so it's better to check them too
				'~/.local/share/Steam/SteamApps/sourcemods',
				'~/Steam/SteamApps/sourcemods'
			}
			for dir in linux_dirs:
				if os_path.isdir(dir):
					return dir
			return None
		except Exception:
			return None

def set_sourcemods_path(path):
	"""
	Set sourcemod folder path.
	"""
	if OS_TYPE == 'Windows':
		global registry
		global registry_key
		if registry == 0:
			registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
			registry_key = winreg.OpenKeyEx(registry, 'SOFTWARE\Valve\Steam')
		
		value = winreg.SetValue(registry_key, 'SourceModInstallPath', winreg.REG_SZ, path)
	

def setup_path():
	"""
	Choose setup path.
	"""
	confirm = False
	vars.SOURCEMODS_PATH = sourcemods_path()
	smodsfound = isinstance(vars.SOURCEMODS_PATH, str)
	if smodsfound:
		gui.message('Sourcemods folder was automatically found at: ' + vars.SOURCEMODS_PATH)
		if gui.message_yes_no('It\'s the recommended installation location. Would you like to install TF2Classic there?'):
			vars.TF2C_PATH = os_path.join(vars.SOURCEMODS_PATH, 'tf2classic')
			confirm = True
		else:
			# check if any sourcemods exists there
			no_sourcemods = True
			for file in os.listdir(vars.SOURCEMODS_PATH):
				if os_path.isdir(file):
					no_sourcemods = False
			
			if no_sourcemods:
				if gui.message_yes_no('Then, would you like to move the sourcemods folder location?'):
					vars.SOURCEMODS_PATH = gui.message_dir('Please enter the location of the new sourcemods folder')
					set_sourcemods_path(vars.SOURCEMODS_PATH)
					vars.TF2C_PATH = os_path.join(vars.SOURCEMODS_PATH, 'tf2classic')
				else:
					gui.message('Then, enter the location in which TF2Classic will be installed to. NOTE: Manual linking or relocation will be required for Steam to see the game!')
					vars.TF2C_PATH = os_path.join(gui.message_dir('location'), 'tf2classic')
	else:
		gui.message('WARNING: Steam\'s sourcemod folder has not been found.')
		if OS_TYPE == 'Windows':
			vars.SOURCEMODS_PATH = 'C:\\Program Files (x86)\\Steam\\steamapps\\sourcemods'
		else:
			vars.SOURCEMODS_PATH = '~/.steam/steam/steamapps/sourcemods/'
		gui.message('The recommended installation location would be ' + vars.SOURCEMODS_PATH + '.')
		if gui.message_yes_no('Would you like to install TF2Classic there?'):
			vars.TF2C_PATH = os_path.join(vars.SOURCEMODS_PATH, 'tf2classic')
			confirm = True
		else:
			vars.TF2C_PATH = os_path.join(gui.message_dir('Please, enter the location in which TF2Classic will be installed to'), 'tf2classic')
		
	if not confirm:
		if not gui.message_yes_no('TF2Classic will be installed in ' + vars.TF2C_PATH + '\nDo you accept?'):
			print('Resetting...\n')
			setup_path()

def setup_binaries():
	"""
	Select paths for required binaries.
	"""
	if OS_TYPE == 'Windows':
		vars.ARIA2C_BINARY = MEIPASS + '/aria2c.exe'
		vars.SEVENZ_BINARY = MEIPASS + '/7za.exe'
	else:
		if shutil.which('aria2c') is None:
			gui.message_end('You need to install Aria2 to use this script.', 1)
		else:
			vars.ARIA2C_BINARY = 'aria2c'

		if which('7zz') is None and which('7z') is None:
			gui.message_end('You need to install 7-Zip or p7zip to use this script.', 1)
		elif which('7zz') is not None:
			vars.SEVENZ_BINARY = '7zz'
		else:
			vars.SEVENZ_BINARY = '7z'