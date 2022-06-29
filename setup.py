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

def setup_path(manual_path):
    """
    Choose setup path.
    """
    confirm = False
    if sourcemods_path() is not None:
        vars.INSTALL_PATH = sourcemods_path().rstrip('\"')

    smodsfound = isinstance(vars.INSTALL_PATH, str)
    if smodsfound is True and manual_path is not True:
        gui.message(lang["setup_found"] % vars.INSTALL_PATH)
        if gui.message_yes_no(lang["setup_found_question"]):
            confirm = True
        else:
            setup_path(True)
    else:
        gui.message(lang["setup_not_found"])
        if gui.message_yes_no(lang["setup_not_found_question"] % getcwd()):
            vars.INSTALL_PATH = getcwd()
            confirm = True
        else:
            vars.INSTALL_PATH = gui.message_dir(lang["setup_input"])

    if not confirm:
        if not gui.message_yes_no(lang["setup_accept"] % vars.INSTALL_PATH):
            print(lang["setup_reset"])
            setup_path(False)

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
            gui.message_end(lang["setup_missing_aria2"], 1)
        else:
            vars.ARIA2C_BINARY = 'aria2c'
        if which('zstd') is None and which('pzstd') is None:
            gui.message_end(lang["setup_missing_zstd"], 1)
        elif which('pzstd') is not None:
            vars.ZSTD_BINARY = 'pzstd'
        else:
            vars.ZSTD_BINARY = 'zstd'
