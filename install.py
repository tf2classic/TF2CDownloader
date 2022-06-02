import subprocess
import os
run = subprocess.run

import gui

def tf2c_download():
	gui.message("Starting the download for TF2Classic 2.0.3... You may see some errors that are safe to ignore.")
	run([ARIA2C_BINARY, "--optimize-concurrent-downloads=true", "--check-certificate=false", "--allow-overwrite=true", "--auto-file-renaming=false", "--continue=true", "--console-log-level=error", "--summary-interval=0", "--bt-hash-check-seed=false", "--seed-time=0", "https://tf2classic.org/tf2c/tf2classic-2.0.3.meta4"], check=True)

def tf2c_extract():
	gui.message("Extracting the downloaded archive...")
	run([SEVENZ_BINARY, "x", "tf2classic-2.0.3.zip", "-aoa"], check=True)
	if not keepzip:
		if os.path.isfile("tf2classic-2.0.3.zip"):
			os.remove("tf2classic-2.0.3.zip")
		if os.path.isfile("tf2classic-2.0.3.meta4"):
			os.remove("tf2classic-2.0.3.meta4")