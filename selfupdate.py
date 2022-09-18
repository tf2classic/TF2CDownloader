"""
Hashes the running binary with SHA-512.
Compares against remote hash that should always point to the latest finished version.
If it doesn't match, prompt to update the game.
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
    elif gui.message_yes_no(_("TF2CDownloader has an update available. Your current version may not work properly. Do you want to install it?")) and not vars.SCRIPT_MODE:
        gui.message_end(_('Delete TF2CDownloader, then redownload and relaunch it from https://tf2classic.com/download')
    elif vars.SCRIPT_MODE:
        gui.message(_("TF2CDownloader out-of-date."))
    else:
        gui.message(_("User chose to skip update. Things may be broken."))
