from subprocess import run
from os import path as os_path, remove as os_remove
from shutil import rmtree
import vars
import gui

def tf2c_download():
	"""
	Download TF2C archive.
	"""
	gui.message('Starting the download for TF2Classic... You may see some errors that are safe to ignore.', 3)
	run([vars.ARIA2C_BINARY, '--optimize-concurrent-downloads=true', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0',
	'-d' + vars.TEMP_PATH,
	'https://wiki.tf2classic.com/misc/tf2classic-latest.meta4'], check=True)

def tf2c_extract():
	"""
	Extract archive and delete it.
	"""
	gui.message('Extracting the downloaded archive...', 1)
	
	run([vars.SEVENZ_BINARY, 'x', os_path.join(vars.TEMP_PATH, 'tf2classic.zip'), '-aoao' + vars.SOURCEMODS_PATH], check=True)
	
	if not vars.keepzip:
		if os_path.isfile(os.path.join(vars.TEMP_PATH, 'tf2classic.zip')):
			os_remove(os.path.join(vars.TEMP_PATH, 'tf2classic.zip'))
		if os_path.isfile(os.path.join(vars.TEMP_PATH, 'tf2classic.meta4')):
			os_remove(os.path.join(vars.TEMP_PATH, 'tf2classic.meta4'))
		rmtree(vars.TEMP_PATH)
