"""
This module is primarily related to helping
the rest of the application find what it needs.

This includes the path to the user's sourcemods
folder, the binary locations for things like Aria2
depending on their platform, etc.
"""
import sys
import os
from platform import system
from shutil import which
from rich import print
import vars
import gui
if system() == 'Windows':
    import winreg


REGISTRY = 0
REGISTRY_KEY = 0

def sourcemods_path():
    """
    Find path to sourcemod folder.
    """
    if system() == 'Windows':
        try:
            global REGISTRY
            global REGISTRY_KEY
            if REGISTRY == 0:
                REGISTRY = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                REGISTRY_KEY = winreg.OpenKeyEx(REGISTRY, r'SOFTWARE\Valve\Steam', access=winreg.KEY_ALL_ACCESS)

            value = winreg.QueryValueEx(REGISTRY_KEY, 'SourceModInstallPath')
            return value[0]
        except Exception:
            return None
    else:
        try:
            sourcepath = None
            with open(os.path.expanduser(r'~/.steam/registry.vdf'), encoding="utf-8") as file:
                for _, line in enumerate(file):
                    if 'SourceModInstallPath' in line:
                        sourcepath = line[line.index('/home'):-1].replace(r'\\', '/')
                        break
                file.close()
            return sourcepath
        except Exception:
            return None

def set_sourcemods_path():
	"""
	Set sourcemod folder path.
	"""
	if not vars.MAKE_SYMLINK:
		return 
	
	try:
		src = vars.SOURCEMODS_PATH
		dest = vars.DEFAULT_SOURCEMODS_PATH
		
		if vars.MOVE_TF2CLASSIC_FOLDER:
			src += "/tf2classic"
			dest += "/tf2classic"
		
		# attempt to remove empty folder, otherwise it'll whine about it
		if os.path.isdir(dest):
			os.rmdir(dest)
		
		# do the symlink
		os.symlink(src, dest)
	except Exception:
		print("Warning: could not create symlink. is the program running with elevated permissions? This only means TF2Classic will have trouble showing up on Steam.");
	
def setup_default_path():
	vars.DEFAULT_SOURCEMODS_PATH = sourcemods_path()
	if vars.DEFAULT_SOURCEMODS_PATH is not None:
		vars.DEFAULT_SOURCEMODS_PATH = sourcemods_path().rstrip('\"')

def setup_path(manual_path):
    """
    Choose setup path.
    """
    confirm = False

	smodsfound = isinstance(vars.DEFAULT_SOURCEMODS_PATH, str)
	if smodsfound and (not manual_path):
		vars.MOVE_TF2CLASSIC_FOLDER = False
		vars.MAKE_SYMLINK = False

		gui.message('Sourcemods folder was automatically found at: ' + vars.DEFAULT_SOURCEMODS_PATH)
		if gui.message_yes_no('It\'s the recommended installation location. Would you like to install TF2Classic there?'):
			vars.SOURCEMODS_PATH = vars.DEFAULT_SOURCEMODS_PATH
			confirm = True
		else:
			# check if any sourcemods exists there
			no_sourcemods = True
			if os.path.exists(vars.DEFAULT_SOURCEMODS_PATH):
				for file in os.listdir(vars.DEFAULT_SOURCEMODS_PATH):
					# there's something in the sourcemods folder, will have to assume it isn't empty
					no_sourcemods = False
					break

			if no_sourcemods:
				if gui.message_yes_no('Then, would you like to move the sourcemods folder location?'):
					vars.SOURCEMODS_PATH = gui.message_dir('Please enter the location of the new sourcemods folder')
					vars.MAKE_SYMLINK = True
				else:
					setup_path(True)
					return
			else:
				setup_path(True)
				return
    else:
		vars.MOVE_TF2CLASSIC_FOLDER = True
		vars.MAKE_SYMLINK = smodsfound

		msg = 'Would you like to install in ' + os.getcwd() + '?'

		if not smodsfound:
			gui.message('WARNING: Steam\'s sourcemods folder has not been found.')
			msg += " You must move it to your sourcemods manually."
		else:
			gui.message('WARNING: You chose not to use the Steam\'s sourcemods folder.')

		if gui.message_yes_no(msg):
            vars.SOURCEMODS_PATH = os.getcwd()
            confirm = True
        else:
            vars.SOURCEMODS_PATH = gui.message_dir('Please, enter the location in which TF2Classic will be installed to.\n')
    # one final confirmation
    if not confirm:
        if not gui.message_yes_no('TF2Classic will be installed in ' + vars.SOURCEMODS_PATH + '\nDo you accept?'):
            print('Resetting...\n')
            setup_path(False)

def setup_binaries():
    """
    Select paths for required binaries.
    """
    if system() == 'Windows':
        # When we can detect that we're compiled using PyInstaller, we use their
        # suggested method of determining the location of the temporary runtime folder
        # to point to Aria2 and Tar.
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            vars.ARIA2C_BINARY = os.path.abspath(os.path.join(os.path.dirname(__file__), 'aria2c.exe'))
            vars.ARC_BINARY = os.path.abspath(os.path.join(os.path.dirname(__file__), 'arc.exe'))
        else:
            # When running as a script, we just select the Binaries folder directly for Aria2 and Tar.
            vars.ARIA2C_BINARY = 'Binaries/aria2c.exe'
            vars.ARC_BINARY = 'Binaries/arc.exe'
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
