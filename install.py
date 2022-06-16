"""
Calls the heavylifting processes to
download and extract the game using the
paths configured in setup.py
"""
from os import path
from platform import system
from shutil import disk_usage, rmtree
from subprocess import run
import gui
import vars


def free_space_check():
    """
    Extracted game is 11GB. Temporary file is 4GB.
    This function makes sure the user has that much
    at the path they're extracting at before moving
    ahead with it.
    """
    minimum_free_download_bytes = 4831838208
    minimum_free_install_bytes = 12884901888
    if disk_usage(vars.TEMP_PATH)[2] < minimum_free_download_bytes:
        gui.message_end("You don't have enough free space to download TF2 Classic. A minimum of 4.5GB on your primary drive is required.", 1)
    if not path.isdir(vars.INSTALL_PATH):
        gui.message_end("The specified extraction location does not exist.", 1)
    elif disk_usage(vars.INSTALL_PATH)[2] < minimum_free_install_bytes:
        gui.message_end("You don't have enough free space to extract TF2 Classic. A minimum of 12GB at your chosen extraction site is required.", 1)

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
    gui.message('Extracting the downloaded archive, please wait patiently.', 1)
    if system() == 'Windows':
        run([vars.ARC_BINARY, '-overwrite', 'unarchive', path.join(vars.TEMP_PATH, 'tf2classic.tar.zst'), vars.INSTALL_PATH], check=True)
    else:
        run(['tar', '-I', vars.ZSTD_BINARY, '-xvf', path.join(vars.TEMP_PATH, 'tf2classic.tar.zst'), '-C', vars.INSTALL_PATH], check=True)
