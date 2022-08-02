"""
UX-related functions, like showing messages,
asking questions, generally handling any sort
of communication or interactivity with the user.
"""
from os import environ, makedirs, path, rmdir
from sys import exit
from time import sleep
from rich import print
from lang import lang


def message(msg, delay = 0):
    """
    Show a message to user.
    Delay stops program for specified amount of seconds.
    """
    print("[bold yellow]" + msg)
    sleep(delay)

def message_yes_no(msg):
    """
    Show a message to user and get yes/no answer.
    """
    # dont know for now how to make it properly, leaving all of pain to future-me
    valid_yes = _("yes y").split()
    valid_no = _("no n").split()
    prompt = _("{y/n}")
    msg += prompt

    while True:
        print(msg)
        choice = input().lower()
        if choice in valid_yes:
            return True
        elif choice in valid_no:
            return False
        else:
            print("[bold blue]" + _("Please respond with 'yes' or 'no' (or 'y' or 'n').") + "[/bold blue]")


def message_input(msg):
    """
    Show a message and get input from user.
    """
    return input(msg + ' > ')

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
        message(_("The specified extraction location does not exist."))

def message_end(msg, code):
    """
    Show a message and exit.
    """
    print("[bold green]" + msg)
    if environ.get("WT_SESSION"):
        print("[bold]" + _("You are safe to close this window."))
    else:
        input(_("Press Enter to exit."))
    exit(code)
