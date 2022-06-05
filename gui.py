from os import path as os_path, makedirs, rmdir
from time import sleep
from sys import exit
from platform import system

def message(msg: str, delay = 0):
	"""
	Show a message to user.
	Delay stops program for specified amount of seconds.
	"""
	print(msg)
	sleep(delay)

def message_yes_no(msg:str, default = True):
	"""
	Show a message to user and get yes/no answer.
	"default" sets "yes" as default answer if true, "no" if false.
	"""
	ans = ''
	ans = input(msg + ' (y (default) / n): ' if default else ' (y / n (default): ')
	if ans == 'y':
		return True
	elif ans == 'n':
		return False
	else:
		return default
	
	
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
		directory = input(msg + ': ')
		if os_path.isdir(directory):
			return directory
		try:
			# wth???
			makedirs(directory)
			rmdir(directory) # lol
			return directory
		except Exception:
			pass

def message_end(msg, code):
	"""
	Show a message and exit.
	"""
	print(msg)
	if system() == 'Windows':
		input('Press Enter to exit.')
	exit(code)
