import subprocess
import os
import shutil
import sys
from time import sleep
run = subprocess.run

def message(msg):
    print(msg)
    if os.name == 'nt':
        sleep(5)

def message_end(msg, code):
    print(msg)
    if os.name == 'nt':
        input("Press any key to exit.")
    sys.exit(code)




if not sys.stdin or not sys.stdin.isatty():
    message_end("Looks like we're running in the background. We don't want that, so we're exiting.")

if os.name == 'nt':
    ARIA2C_BINARY = sys._MEIPASS + "/aria2c.exe"
    SEVENZ_BINARY = sys._MEIPASS + "/7za.exe"
else:
    if shutil.which("aria2c") is None:
        message_end("You need to install Aria2 to use this script.", 1)
    else:
        ARIA2C_BINARY = "aria2c"

    if shutil.which("7zz") is None and shutil.which("7z") is None:
        message_end("You need to install 7-Zip or p7zip to use this script.", 1)
    elif shutil.which("7zz") is not None:
        SEVENZ_BINARY = "7zz"
    else:
        SEVENZ_BINARY = "7z"

message("Starting the download for TF2Classic 2.0.3... You may see some errors that are safe to ignore.")
run([ARIA2C_BINARY, "--optimize-concurrent-downloads=true", "--check-certificate=false", "--allow-overwrite=true", "--auto-file-renaming=false", "--continue=true", "--console-log-level=error", "--summary-interval=0", "--bt-hash-check-seed=false", "--seed-time=0", "https://tf2classic.org/tf2c/tf2classic-2.0.3.meta4"], check=True)

message("Extracting the downloaded archive...")
run([SEVENZ_BINARY, "x", "tf2classic-2.0.3.zip", "-aoa"], check=True)
if os.path.isfile("tf2classic-2.0.3.zip"):
    os.remove("tf2classic-2.0.3.zip")
if os.path.isfile("tf2classic-2.0.3.meta4"):
    os.remove("tf2classic-2.0.3.meta4")
message_end("Extraction finished.", 0)
