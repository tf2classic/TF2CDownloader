"""
Master module. Runs basic checks and then offloads all
of the real work to functions defined in other files.
"""
import os
import traceback
import ctypes
from platform import system
from shutil import which
from subprocess import run
from sys import argv, exit, stdin
from rich import print
from lang import lang
import gui
import install
import setup

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
        print(lang["running_background"])
        exit(1)
try:
    sanity_check()
    setup.setup_path(False)
    setup.setup_binaries()
    install.free_space_check()
    install.tf2c_download()
    install.tf2c_extract()
except Exception as ex:
    if ex is not SystemExit:
        traceback.print_exc()
        print(lang["exception_line"])
        print(lang["exception"])
        if os.environ.get("WT_SESSION"):
            print(lang["exit_safe"])
        else:
            input(lang["exit"])
        exit(1)


gui.message_end(lang["success"], 0)
