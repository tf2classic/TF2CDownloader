"""
Tiny module that currently just establishes
the temp paths and some variables for other
modules to use.
"""
from platform import system
import tempfile

if system() == 'Windows':
    TEMP_PATH = tempfile.gettempdir()
else:
    TEMP_PATH = '/var/tmp/'

ARIA2C_BINARY = None
# ZSTD_BINARY is only used on Linux.
ZSTD_BINARY = None
INSTALL_PATH = None
# ARC_BINARY is only used on Windows.
ARC_BINARY = None
TF2C_PATH = None
