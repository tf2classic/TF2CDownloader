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
        gui.message('Sourcemods folder was automatically found at: ' + vars.INSTALL_PATH)
        if gui.message_yes_no('It\'s the recommended installation location. Would you like to install TF2Classic there?'):
            confirm = True
        else:
            setup_path(True)
    else:
        gui.message('WARNING: Steam\'s sourcemods folder has not been found, or you chose not to use it.')
        if gui.message_yes_no('Would you like to extract in ' + getcwd() + '? You must move it to your sourcemods manually.'):
            vars.INSTALL_PATH = getcwd()
            confirm = True
        else:
            vars.INSTALL_PATH = gui.message_dir('Please, enter the location in which TF2Classic will be installed to.\n')

    if not confirm:
        if not gui.message_yes_no('TF2Classic will be installed in ' + vars.INSTALL_PATH + '\nDo you accept?'):
            print('Resetting...\n')
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
            vars.TAR_BINARY = path.abspath(path.join(path.dirname(__file__), 'tar.exe'))
            # For whatever reason, Tar won't load Zstd when we give it the path
            # to the file like the others. So, we instead add PyInstaller's temp folder to
            # Windows' PATH, or if we're running as a script, the Binaries folder instead,
            # so that Tar only needs to call the executable name.
            #
            # This is terrible. Someone needs to fix this.
            environ['PATH'] += path.join(path.dirname(__file__))
        else:
            # When running as a script, we just select the Binaries folder directly for Aria2 and Tar.
            vars.ARIA2C_BINARY = 'Binaries/aria2c.exe'
            vars.TAR_BINARY = 'Binaries/tar.exe'
            environ['PATH'] += path.join(path.dirname(__file__) + r'/Binaries/')
    else:
        vars.TAR_BINARY = 'tar'
        if which('aria2c') is None:
            gui.message_end('You need to install Aria2 to use this script.', 1)
        else:
            vars.ARIA2C_BINARY = 'aria2c'
        if which('zstd') is None and which('pzstd') is None:
            gui.message_end('You need to install Zstd to use this script.', 1)
        elif which('pzstd') is not None:
            vars.ZSTD_BINARY = 'pzstd'
        else:
            vars.ZSTD_BINARY = 'zstd'
