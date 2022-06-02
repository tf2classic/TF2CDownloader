import subprocess
import os
import shutil
import sys
from time import sleep
run = subprocess.run
if not sys.stdin or not sys.stdin.isatty():
    print("Looks like we're running in the background. We don't want that, so we're exiting.")
    sys.exit()

if os.name == 'nt':
    ARIA2C_BINARY = sys._MEIPASS + "/aria2c.exe"
    SEVENZ_BINARY = sys._MEIPASS + "/7za.exe"
else:
    if shutil.which("aria2c") is None:
        print("You need to install Aria2 to use this script.")
        sys.exit()
    else:
        ARIA2C_BINARY = "aria2c"

    if shutil.which("7zz") is None and shutil.which("7z") is None:
        print("You need to install 7-Zip or p7zip to use this script.")
        sys.exit()
    elif shutil.which("7zz") is not None:
        SEVENZ_BINARY = "7zz"
    else:
        SEVENZ_BINARY = "7z"

print("Starting the download for TF2Classic 2.0.3 in five seconds. You may see some errors that are safe to ignore.")
sleep(5)
run([ARIA2C_BINARY, "--optimize-concurrent-downloads=true", "--check-certificate=false", "--allow-overwrite=true", "--auto-file-renaming=false", "--continue=true", "--console-log-level=error", "--summary-interval=0", "--bt-hash-check-seed=false", "--seed-time=0", "https://tf2classic.org/tf2c/tf2classic-2.0.3.meta4"], check=True)
print("Extracting the downloaded archive in five seconds.")
sleep(5)
run([SEVENZ_BINARY, "x", "tf2classic-2.0.3.zip", "-aoa"], check=True)
if os.path.isfile("tf2classic-2.0.3.zip"):
    os.remove("tf2classic-2.0.3.zip")
if os.path.isfile("tf2classic-2.0.3.meta4"):
    os.remove("tf2classic-2.0.3.meta4")
print("Extraction finished. You can close this window at any time, or it will exit in thirty seconds.")
sleep(30)
sys.exit()
