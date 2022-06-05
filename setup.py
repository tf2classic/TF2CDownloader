from os import path as os_path
from shutil import which
from sys import _MEIPASS as MEIPASS
from platform import system
if system() == 'Windows':
	import winreg
import vars
import gui

registry = 0
registry_key = 0

def sourcemods_path():
	"""
	Find path to sourcemod folder.
	"""
	if system() == 'Windows':
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
			sourcepath = None
			with open(os_path.expanduser('~/.steam/registry.vdf'), 'r') as file:
				for _, line in enumerate(file):
					if 'SourceModInstallPath' in line:
						sourcepath = line[line.index('/home'):-1].replace(r'\\', '/')
						break
				file.close()
			return sourcepath
		except Exception:
			return None

def set_sourcemods_path(path):
	"""
	Set sourcemod folder path.
	"""
	if system() == 'Windows':
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
	vars.SOURCEMODS_PATH = sourcemods_path().rstrip('\"')
	
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
		if system() == 'Windows':
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
	if system() == 'Windows':
		vars.ARIA2C_BINARY = MEIPASS + '/aria2c.exe'
		vars.ZSTD_BINARY = MEIPASS + '/pzstd.exe'
	else:
		if which('aria2c') is None:
			gui.message_end('You need to install Aria2 to use this script.', 1)
		else:
			vars.ARIA2C_BINARY = 'aria2c'

		if which('zstd') is None and which('pzstd') is None:
			gui.message_end('You need to install Zstd to use this script.', 1)
		elif which('pzstd') is not None:
			vars.ZSTD_BINARY = 'pzstd'
		else:
			vars.ZSTD_BINARY = 'zstd'
