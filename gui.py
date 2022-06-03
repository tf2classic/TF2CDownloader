import os
from time import sleep
import sys

def message(msg):
	print(msg)
	print()
	if os.name == 'nt':
		sleep(5)

def message_quick(msg):
	print(msg)

def message_yes_no(msg):
	ans = None
	while ans not in ("y", "n"):
		ans = input(msg + " (Y/N)>").lower()
	
	if ans == "y":
		return True
	elif ans == "n":
		return False
	
def message_input(msg):
	return input(msg + " >")

def message_dir(msg):
	while True:
		directory = input(msg + ": ")
		if os.path.isdir(directory):
			return directory
		try:
			os.makedirs(directory)
			os.rmdir(directory) # lol
			return directory
		except Exception:
			pass

def message_end(msg, code):
    print(msg)
    if os.name == 'nt':
        input("Press Enter to exit.")
    sys.exit(code)
