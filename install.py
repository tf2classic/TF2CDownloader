from subprocess import run
from os import path as os_path, remove as os_remove
from shutil import rmtree, disk_usage
from platform import system
import vars
import gui

def free_space_check():
	"""
	Extracted game is 11GB. Temporary file is 4GB.
	This function makes sure the user has that much
	at the path they're extracting at before moving
	ahead with it.
	"""
	MINIMUM_FREE_BYTES = 16106127360
	if os_path.isdir(vars.SOURCEMODS_PATH) == False:
		gui.message_end("The specified extraction location does not exist.", 1)
	elif disk_usage(vars.SOURCEMODS_PATH)[2] < MINIMUM_FREE_BYTES:
		gui.message_end("You don't have enough free space to install TF2 Classic. A minimum of 15GB is required.", 1)

def tf2c_download():
	"""
	Download TF2C archive.
	"""
	gui.message('Starting the download for TF2 Classic... You may see some errors that are safe to ignore.', 3)
	run([vars.ARIA2C_BINARY, '--max-connection-per-server=16', '--max-concurrent-downloads=16', '--optimize-concurrent-downloads=true', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0',
	'-d' + vars.TEMP_PATH,
	'https://wiki.tf2classic.com/misc/tf2classic-latest-zst.meta4'], check=True)

def tf2c_extract():
	"""
	Extract archive and delete it.
	"""
	gui.message('Extracting the downloaded archive...', 1)
	if system() == 'Windows':
		run([vars.TAR_BINARY, '-I', 'zstd.exe', '-xvf', os_path.join(vars.TEMP_PATH, 'tf2classic.tar.zst'), '-C', vars.SOURCEMODS_PATH], check=True)
	else:
		run([vars.TAR_BINARY, '-I', vars.ZSTD_BINARY, '-xvf', os_path.join(vars.TEMP_PATH, 'tf2classic.tar.zst'), '-C', vars.SOURCEMODS_PATH], check=True)
	
	if not vars.keepzip:
		rmtree(vars.TEMP_PATH)
