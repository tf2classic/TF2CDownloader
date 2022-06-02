import subprocess
import os
run = subprocess.run

import vars
import gui

def tf2c_download():
	gui.message("Starting the download for TF2Classic... You may see some errors that are safe to ignore.")
	run([vars.ARIA2C_BINARY, "--optimize-concurrent-downloads=true", "--check-certificate=false", "--allow-overwrite=true", "--auto-file-renaming=false", "--continue=true", "--console-log-level=error", "--summary-interval=0", "--bt-hash-check-seed=false", "--seed-time=0",
	"-d" + vars.TEMP_PATH,
	"https://tf2classic.org/tf2c/tf2classic.meta4"], check=True)
	
	# find whatever zip file it made and rename it
	
	dircontent = os.listdir(vars.TEMP_PATH)
	for file in dircontent:
		if file.endswith(".zip") and os.path.isfile(vars.TEMP_PATH + file):
			os.rename(vars.TEMP_PATH + file, vars.TEMP_PATH + "tf2classic.zip")
			break;

def tf2c_extract(path):
	gui.message("Extracting the downloaded archive...")
	run([vars.SEVENZ_BINARY, "x", vars.TEMP_PATH + "tf2classic.zip", "-aoa"], check=True)
	if not vars.keepzip:
		if os.path.isfile(vars.TEMP_PATH + "tf2classic.zip"):
			os.remove(vars.TEMP_PATH + "tf2classic.zip")
		if os.path.isfile(vars.TEMP_PATH + "tf2classic.meta4"):
			os.remove(vars.TEMP_PATH + "tf2classic.meta4")
		os.rmdir(vars.TEMP_PATH)