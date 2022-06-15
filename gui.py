"""
UX-related functions, like showing messages,
asking questions, generally handling any sort
of communication or interactivity with the user.
"""
from os import environ, makedirs, path, rmdir
from sys import exit
from time import sleep
from rich import print


def message(msg, delay = 0):
    """
    Show a message to user.
    Delay stops program for specified amount of seconds.
    """
    print("[bold yellow]" + msg)
    sleep(delay)

def message_yes_no(msg, default = None):
    """
    Show a message to user and get yes/no answer.
    """
    valid = {"yes": True, "y": True, "no": False, "n": False}
    prompt = {None: " {y/n}", "y": " {Y/n}", "n": " {y/N}"}[default]
    msg += prompt

    while True:
        print(msg)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("[bold blue]Please respond with 'yes' or 'no' (or 'y' or 'n').[/bold blue]")


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
        print("[bold]You are safe to close this window.")
    else:
        input("Press Enter to exit.")
    exit(code)
