# TF2CDownloader
Simple script for downloading and extracting TF2Classic quickly, simply, and efficiently.


Won't function right on Windows unless it's compiled by PyInstaller, as it's hardcoded to use a variable only supplied to it *by* PyInstaller in order to find the Binaries folder.

In the Binaries folder of the repository, Aria2 and its relevant dependencies are extracted from: https://github.com/q3aql/aria2-static-builds (aria2-1.36.0-win-64bit-build2.7z)

Zstd is extracted from https://github.com/facebook/zstd/releases/download/v1.5.2/zstd-v1.5.2-win64.zip

The contents of this folder can be freely replaced with your own builds of these tools, as long as aria2c.exe and pzstd.exe are present.
