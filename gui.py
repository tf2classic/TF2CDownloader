"""
UX-related functions, like showing messages,
asking questions, generally handling any sort
of communication or interactivity with the user.
"""
from os import environ, makedirs, path, rmdir
from sys import exit
from time import sleep
from rich import print
from gettext import gettext as _
import unicodedata
import vars

def message(msg, delay = 0):
    """
    Show a message to user.
    Delay stops program for specified amount of seconds.
    """
    print("[bold yellow]" + msg)
    if not vars.SCRIPT_MODE:
        sleep(delay)

def message_yes_no(msg, default = None):
    """
    Show a message to user and get yes/no answer.
    """
    if vars.SCRIPT_MODE:
        return default

    valid = {}
    valid["yes"] = True
    valid["no"] = False
    valid["y"] = True
    valid["n"] = False

    localyes = _("yes")
    localno = _("no")
    valid[localyes] = True
    valid[localyes[0]] = True
    valid[localno] = False
    valid[localno[0]] = False

    prompt = _(" {y/n}")
    if default == "y":
        prompt = _(" {Y/n}")
    elif default == "n":
        prompt = _(" {y/N}")
    msg += prompt

    while True:
        print(msg)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print(_("[bold blue]Please respond with 'yes' or 'no' (or 'y' or 'n').[/bold blue]"))


def message_input(msg):
    """
    Show a message and get input from user.
    """
    return input(msg + ' >')

def message_dir(msg):
    """
    Show a message and ask for a directory.
    """
    while True:
        dir = input(msg + ": ")
        if dir.count("~") > 0:
            dir = path.expanduser(dir)
        if dir.count("$") > 0:
            dir = path.expandvars(dir)
        if path.isdir(dir):
            return dir
        try:
            makedirs(dir)
            rmdir(dir)
            return dir
        except Exception:
            pass

def message_end(msg, code):
    """
    Show a message and exit.
    """
    print("[bold green]" + msg)
    if environ.get("WT_SESSION"):
        print(_("[bold]You are safe to close this window."))
    else:
        input(_("Press Enter to exit."))
    exit(code)
