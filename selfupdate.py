"""
Hashes the running binary with SHA-512.
Compares against remote hash that should always point to the latest finished version.
If it doesn't match, prompt to update, which means redownloading the latest GH release over the local copy, then relaunching.
"""

from sys import argv
from subprocess import run
from platform import system
from gettext import gettext as _
import hashlib
import urllib.request
import os
import sys
import gui
import vars

def hash_script():
    h = hashlib.sha512()
    with open(argv[0], 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def check_downloader_update():
    remote_hash = urllib.request.urlopen("https://wiki.tf2classic.com/testing/sha512sum")
    remote_hash_bytes = remote_hash.read()
    remote_hash_string = remote_hash_bytes.decode("utf8")
    remote_hash_string = remote_hash_string.rstrip('\n')
    remote_hash.close()

    if remote_hash_string == hash_script():
        gui.message(_("TF2CDownloader appears to be up-to-date."))
    elif gui.message_yes_no(_("TF2CDownloader has an update available. Do you want to install it?")) and not vars.SCRIPT_MODE:
        return 'update_d'
    elif vars.SCRIPT_MODE:
        gui.message(_("Update available, automatically downloading and relaunching since we're running non-interactively.")
        return 'update_d'
    else:
        gui.message(_("User chose to skip update. Things may be broken."))

def apply_downloader_update():
    if system() == 'Windows':
        run([vars.ARIA2C_BINARY, '--max-connection-per-server=16', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0', '-d' + os.getcwd(), 'https://github.com/tf2classic/TF2CDownloader/releases/latest/download/TF2CDownloaderWindows.exe'], check=True)
    else:
        run([vars.ARIA2C_BINARY, '--max-connection-per-server=16', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0', '-d' + os.getcwd(), 'https://github.com/tf2classic/TF2CDownloader/releases/latest/download/TF2CDownloaderLinux'], check=True)
    os.execv(sys.argv[0], sys.argv)




