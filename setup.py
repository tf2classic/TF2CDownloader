"""
This module is primarily related to helping
the rest of the application find what it needs.
This includes the path to the user's sourcemods
folder, the binary locations for things like Aria2
depending on their platform, etc.
"""
import sys
from os import environ, getcwd, path
from platform import system
from shutil import which
from rich import print
from lang import lang
import gui
import vars
if system() == 'Windows':
    import winreg


REGISTRY = 0
REGISTRY_KEY = 0

def sourcemods_path():
    """
    Find path to sourcemod folder.
    """
    if system() == 'Windows':
        try:
            global REGISTRY
            global REGISTRY_KEY
            if REGISTRY == 0:
                REGISTRY = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                REGISTRY_KEY = winreg.OpenKeyEx(REGISTRY, r'SOFTWARE\Valve\Steam', access=winreg.KEY_ALL_ACCESS)

            value = winreg.QueryValueEx(REGISTRY_KEY, 'SourceModInstallPath')
            return value[0]
        except Exception:
            return None
    else:
        try:
            sourcepath = None
            with open(path.expanduser(r'~/.steam/registry.vdf'), encoding="utf-8") as file:
                for _, line in enumerate(file):
                    if 'SourceModInstallPath' in line:
                        sourcepath = line[line.index('/home'):-1].replace(r'\\', '/')
                        break
                file.close()
            return sourcepath
        except Exception:
            return None

def setup_path():
    """
    Choose setup path.
    """
    vars.INSTALL_PATH = sourcemods_path().rstrip('\"')
    if isinstance(vars.INSTALL_PATH, str):
        gui.message(_("Sourcemods folder was automatically found at: %s") % vars.INSTALL_PATH)
        if gui.message_yes_no(_("It's the recommended installation location. Would you like to install TF2 Classic there?")):
            return
    else:
        gui.message(_("WARNING: Steam's sourcemods folder has not been found."))
    
    current = getcwd()
    if gui.message_yes_no(_("Would you like to extract in %s? You must move it to your sourcemods manually.") % current):
        vars.INSTALL_PATH = current
    else:
        vars.INSTALL_PATH = gui.message_dir(_("Please, enter the location in which TF2 Classic will be installed to.\n"))
        while not gui.message_yes_no(_("TF2 Classic will be installed in %s\nDo you accept?") % vars.INSTALL_PATH):
            vars.INSTALL_PATH = gui.message_dir()

def setup_binaries():
    """
    Select paths for required binaries.
    """
    if system() == 'Windows':
        # When we can detect that we're compiled using PyInstaller, we use their
        # suggested method of determining the location of the temporary runtime folder
        # to point to Aria2 and Tar.
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            vars.ARIA2C_BINARY = path.abspath(path.join(path.dirname(__file__), 'aria2c.exe'))
            vars.ARC_BINARY = path.abspath(path.join(path.dirname(__file__), 'arc.exe'))
        else:
            # When running as a script, we just select the Binaries folder directly for Aria2 and Arc.
            vars.ARIA2C_BINARY = 'Binaries/aria2c.exe'
            vars.ARC_BINARY = 'Binaries/arc.exe'
    else:
        if which('aria2c') is None:
            gui.message_end(_("You need to install Aria2 to use this script."), 1)
        else:
            vars.ARIA2C_BINARY = 'aria2c'
        if which('zstd') is None and which('pzstd') is None:
            gui.message_end(_("You need to install Zstd to use this script."), 1)
        elif which('zstd') is not None:
            vars.ZSTD_BINARY = 'zstd'
        else:
            vars.ZSTD_BINARY = 'pzstd'
