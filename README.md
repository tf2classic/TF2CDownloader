# TF2CDownloader
Simple script for downloading and extracting TF2Classic quickly, simply, and efficiently.


Won't function right on Windows unless it's compiled by PyInstaller, as it's hardcoded to use a variable only supplied to it *by* PyInstaller in order to find the Binaries folder.

In the Binaries folder of the repository, Aria2 and its relevant dependencies are from MSYS2: https://packages.msys2.org/package/mingw-w64-x86_64-aria2

7za.exe is extracted from 7-Zip Extra 21.07: https://www.7-zip.org/a/7z2107-extra.7z

The contents of this folder can be freely replaced with your own builds of these tools, as long as aria2c.exe and 7za.exe are present.
