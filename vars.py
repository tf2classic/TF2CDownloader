"""
Tiny module that currently just establishes
the temp paths and some variables for other
modules to use.
"""
from platform import system
import tempfile

TEMP_PATH = tempfile.gettempdir()

ARIA2C_BINARY = None
# ZSTD_BINARY is only used on Linux.
ZSTD_BINARY = None
# ARC_BINARY is only used on Windows.
ARC_BINARY = None
SOURCEMODS_PATH = None
TF2C_PATH = None
