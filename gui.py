import os
from time import sleep
import sys

def message(msg):
    print(msg)
    if os.name == 'nt':
        sleep(5)

def message_end(msg, code):
    print(msg)
    if os.name == 'nt':
        input("Press Enter to exit.")
    sys.exit(code)
