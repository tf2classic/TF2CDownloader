import gui
import subprocess
import os
import vars
import shutil

run = subprocess.run

def tf2c_download():
	gui.message("Starting the download for TF2Classic... You may see some errors that are safe to ignore.")
	run([vars.ARIA2C_BINARY, "--optimize-concurrent-downloads=true", "--check-certificate=false", "--allow-overwrite=true", "--auto-file-renaming=false", "--continue=true", "--console-log-level=error", "--summary-interval=0", "--bt-hash-check-seed=false", "--seed-time=0",
	"-d" + vars.TEMP_PATH,
	"https://wiki.tf2classic.com/misc/tf2classic-latest.meta4"], check=True)

def tf2c_extract():
	gui.message("Extracting the downloaded archive...")
	run([vars.SEVENZ_BINARY, "x", vars.TEMP_PATH + "tf2classic.zip", "-aoa"], check=True)
	if not vars.keepzip:
		if os.path.isfile(vars.TEMP_PATH + "tf2classic.zip"):
			os.remove(vars.TEMP_PATH + "tf2classic.zip")
		if os.path.isfile(vars.TEMP_PATH + "tf2classic-latest.meta4"):
			os.remove(vars.TEMP_PATH + "tf2classic-latest.meta4")
		shutil.rmtree(vars.TEMP_PATH)
