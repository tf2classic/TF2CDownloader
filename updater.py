import gui
import vars
import os.path
import urllib.request
from gettext import gettext as _
VERSION_LIST = urllib.request.urlopen('https://tf2classic.org/updater/versions.py')
exec(VERSION_LIST.read())

def update_version_file():
    """
    The previous launcher/updater leaves behind a rev.txt file with the old internal revision number.
    To avoid file bloat, we reuse this, but replace it with the game's semantic version number.
    To obtain the game's semantic version number, we do some horrible parsing of the game's version.txt
    file, which is what the game itself uses directly to show the version number on the main menu, etc.
    
    This parsing and migration is only necessary for older builds of the game, as rev.txt should be updated
    as a part of the installation process on 2.0.4/2.1.0 and newer.
    """
    old_version_file = open(vars.INSTALL_PATH + '/tf2classic/version.txt', 'r')
    old_version = old_version_file.readlines()[1]
    before, sep, after = old_version.partition('=')
    if len(after) > 0:
        old_version = after
    old_version = old_version.replace('.', '')

    # Matching to codenames - should only be necessary up to 2.0.3
    new_version_file = open(vars.INSTALL_PATH + '/tf2classic/rev.txt', 'w')
    if old_version < "204":
        new_version_file.write(old_version)
    else:
        gui.message(_("No migration necessary!"), 1)
    new_version_file.close()
    old_version_file.close()

def check_for_updates():
    """
    It's all math here. We can compare the minimized semantic version number against remote variables to see what we should do.
    """
    local_version_file = open(vars.INSTALL_PATH + '/tf2classic/rev.txt', 'r')
    local_version = local_version_file.read()
    local_version = int(local_version)

    if local_version == LATEST_VER:
        if gui.message_yes_no(_("We found an existing up-to-date installation of the game. Do you want to repair it?"), False):
            return 'reinstall'
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)
            
    if local_version == PREVIOUS_VER:
        if gui.message_yes_no(_("An update is available for your game. Do you want to install it?"), 0):
            return 'update'
        else:
            if gui.message_yes_no(_("In that case, do you want to reinstall completely?"), 0):
                return 'reinstall'
            else:
                gui.message_end(_("We have nothing to do. Goodbye!"), 0)
        
    # We're only generating archives for single-step updates. If the user is more than one version out-of-date, better off reinstalling.
    if local_version < PREVIOUS_VER:
        if gui.message_yes_no(_("An update is available for your game. Do you want to install it?"), 0):
            return 'reinstall'
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)

def update():
    """
    The simplest part of all this - if this function is called, we know the user wants to update.
    """
    gui.message(_("Downloading the update archive..."), 3)
    
    # The same line that installs the game in install.py, just a different URL. Could probably unify into a single function.
    run([vars.ARIA2C_BINARY, '--max-connection-per-server=16', '-UTF2CDownloaderGit', '--max-concurrent-downloads=16', '--optimize-concurrent-downloads=true', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0',
    '-d' + vars.TEMP_PATH,
    PREV_TO_LATEST_DL], check=True)
    
    # The same line that extracts the game in install.py, just a different file path. Could probably unify into a single function.
    gui.message(_("Extracting the downloaded archive, please wait patiently."), 1)
    if system() == 'Windows':
        run([vars.ARC_BINARY, '-overwrite', 'unarchive', path.join(vars.TEMP_PATH, 'tf2classic-patch.tar.zst'), vars.INSTALL_PATH], check=True)
    else:
        run(['tar', '-I', vars.ZSTD_BINARY, '-xvf', path.join(vars.TEMP_PATH, 'tf2classic-patch.tar.zst'), '-C', vars.INSTALL_PATH], check=True)
