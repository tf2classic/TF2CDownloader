z"""
Master module. Runs basic checks and then offloads all
of the real work to functions defined in other files.
"""
import os
import traceback
import ctypes
from platform import system
from shutil import which
from subprocess import run
import sys
from sys import argv, exit, stdin
from rich import print
from gettext import gettext as _
import gettext
import gui
import install
import setup
import troubleshoot
import updater
import vars

# PyInstaller offers no native way to select which application you use for the console.
# Instead, it uses the system default, which is cmd.exe at time of writing.
# This hack checks if Windows Terminal is installed. If it is, and if the application
# is launched with cmd.exe instead, it relaunches the application in WT instead.
if system() == 'Windows':
    if which('wt') is not None and os.environ.get("WT_SESSION") is None:
        run(['wt', argv[0]], check=True)    
        exit()

# Disable QuickEdit so the process doesn't pause when clicked
if system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))

def sanity_check():
    """
    This is mainly for Linux, because it's easy to launch it by double-clicking it, which would
    run it in the background and not show any output. PyInstaller has no way to force a terminal
    open for this on Linux. We could implement something similar to what we do to force using WT,
    but it's not a priority right now since Linux users can figure out how to use the terminal.
    """
    if not stdin or not stdin.isatty():
        print(_("Looks like we're running in the background. We don't want that, so we're exiting."))
        exit(1)

if sys.stdout.encoding == 'ascii':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding == 'ascii':
    sys.stderr.reconfigure(encoding='utf-8')

if os.getenv('LANG') is None:
    import locale
    lang, enc = locale.getdefaultlocale()
    os.environ['LANG'] = lang

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    gettext.bindtextdomain('tf2c-downloader', os.path.abspath(os.path.join(os.path.dirname(__file__), 'locale')))
else:
    gettext.bindtextdomain('tf2c-downloader', 'locale')
gettext.textdomain('tf2c-downloader')

try:
    sanity_check()
    setup.setup_path(False)
    setup.setup_binaries()
    # After this line, we have two possible paths: installing, or updating/repairing
    if os.path.exists(vars.INSTALL_PATH + '/tf2classic/gameinfo.txt'):
        vars.INSTALLED = True
    if vars.INSTALLED == True:
        updater.update_version_file()
    if updater.check_for_updates() == 'reinstall' or vars.INSTALLED == False:
        install.free_space_check()
        install.tf2c_download()
        install.tf2c_extract()
        troubleshoot.apply_blacklist()
    else:
        install.free_space_check()
        updater.update()
except Exception as ex:
    if ex is not SystemExit:
        traceback.print_exc()
        print(_("[italic magenta]----- Exception details above this line -----"))
        print(_("[bold red]:warning: The program has failed. Post a screenshot in #technical-issues on the Discord. :warning:[/bold red]"))
        if os.environ.get("WT_SESSION"):
            print(_("[bold]You are safe to close this window."))
        else:
            input(_("Press Enter to exit."))
        exit(1)


gui.message_end(_("The installation has successfully completed. Remember to restart Steam!"), 0)
