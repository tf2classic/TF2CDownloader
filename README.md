# TF2CDownloader
To end-users, this tool is the official installer and updater for Team Fortress 2 Classic. 

To programmers, this is a thin and rough script that sits on top of Aria2 and Butler to provide reasonably-efficient updating without too much complication.

To other Sourcemods, this is a tool you can use for *your project* with only minor work, as the mechanism here is extremely agnostic and flexible. Get in touch with cco on our Discord if you're interested!

----

Requires Rich, PyZstd, TQDM, and HTTPX to build.

PyInstaller is used to build this into a single-file binary. A spec file is included.

For convenience in building, the Binaries folder of the repository contains prebuilt and static versions of Aria2 and Butler for Windows and Linux. Aria2 is extracted from here: https://github.com/q3aql/aria2-static-builds (aria2-1.36.0-win-64bit-build2.7z)

The official build of Butler, as supplied by itch.io, is used.

----

<a href="https://hosted.weblate.org/engage/tf2cdownloader/">
<img src="https://hosted.weblate.org/widgets/tf2cdownloader/-/287x66-grey.png" alt="Translation status" />
</a>
