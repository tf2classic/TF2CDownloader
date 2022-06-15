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
MAKE_SYMLINK = False
MOVE_TF2CLASSIC_FOLDER = False
DEFAULT_SOURCEMODS_PATH = None
