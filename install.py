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
	run([vars.ARIA2C_BINARY, '--max-connection-per-server=16', '--max-concurrent-downloads=16', '--optimize-concurrent-downloads=true', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0',
	'-d' + vars.TEMP_PATH,
	'https://wiki.tf2classic.com/misc/tf2classic-latest-zst.meta4'], check=True)

def tf2c_extract():
	"""
	Extract archive and delete it.
	"""
	gui.message('Extracting the downloaded archive...', 1)
	
	run([vars.TAR_BINARY, '-I', vars.ZSTD_BINARY + ' -p1', '-xvf', os_path.join(vars.TEMP_PATH, 'tf2classic.tar.zst'), '-C', vars.SOURCEMODS_PATH], check=True)
	
	if not vars.keepzip:
		rmtree(vars.TEMP_PATH)
