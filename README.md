# TF2CDownloader
Simple script for downloading and extracting TF2Classic quickly, simply, and efficiently.

Won't function right on Windows unless it's compiled by PyInstaller, as it's hardcoded to use a variable only supplied by it in order to find the binaries it needs.

Compile for Linux with: `pyinstaller --onefile TF2CDownloader.py`

Compile for Windows with: `pyinstaller --onefile --add-data="Binaries/*;." --icon=tf2c.ico TF2CDownloader.py`
