from os import path
from subprocess import run
from platform import system
from gettext import gettext as _
from gettext import ngettext as _N
from shutil import disk_usage
from tqdm import tqdm
import vars
import gui
import versions
import pyzstd
import tarfile
import os

def download_extract(url, filename, endpath):
    run([vars.ARIA2C_BINARY, '--max-connection-per-server=16', '-UTF2CDownloader2022-12-04-1', '--max-concurrent-downloads=16', '--optimize-concurrent-downloads=true', '--check-certificate=false', '--check-integrity=true', '--auto-file-renaming=false', '--continue=true', '--console-log-level=error', '--summary-interval=0', '--bt-hash-check-seed=false', '--seed-time=0',
    '-d' + vars.TEMP_PATH, url], check=True)

    gui.message(_("Extracting the downloaded archive, please wait patiently."), 1)
    class ZstdTarFile(tarfile.TarFile):
        def __init__(self, name, mode='r', *, level_or_option=None, zstd_dict=None, **kwargs):
            self.zstd_file = pyzstd.ZstdFile(name, mode,
                                    level_or_option=level_or_option,
                                    zstd_dict=zstd_dict)
            try:
                super().__init__(fileobj=self.zstd_file, mode=mode, **kwargs)
            except:
                self.zstd_file.close()
                raise
    
        def close(self):
            try:
                super().close()
            finally:
                self.zstd_file.close()

    # read .tar.zst file (decompression)
    with ZstdTarFile(path.join(vars.TEMP_PATH, filename), mode='r') as tar:
        for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
            tar.extract(member=member, path=endpath)

def pretty_size(bytes):
    if bytes < 100:
        return _N("%s byte", "%s bytes", bytes) % bytes
    elif bytes < 1000000:
        return _("%.2f kB") % (bytes/1000)
    elif bytes < 1000000000:
        return _("%.2f MB") % (bytes/1000000)
    elif bytes < 1000000000000:
        return _("%.2f GB") % (bytes/1000000000)
    elif bytes < 1000000000000000:
        return _("%.2f TB") % (bytes/1000000000000)
    elif bytes < 1000000000000000000:
        return _("%.2f PB") % (bytes/1000000000000000)

def free_space_check(presz, postsz):
    if disk_usage(vars.TEMP_PATH)[2] < presz:
        gui.message_end(_("You don't have enough free space for the download. A minimum of %s on your primary drive is required.") % pretty_size(presz), 1)
    if not path.isdir(vars.INSTALL_PATH):
        gui.message_end(_("The specified extraction location does not exist."), 1)
    elif disk_usage(vars.INSTALL_PATH)[2] < postsz and vars.INSTALLED == False:
        gui.message_end(_("You don't have enough free space for the extraction. A minimum of %s at your chosen extraction site is required.") % pretty_size(postsz), 1)

def prepare_symlink():
    for s in vars.TO_SYMLINK:
        if path.isfile(vars.INSTALL_PATH + s[1]) and not path.islink(vars.INSTALL_PATH + s[1]):
            os.remove(vars.INSTALL_PATH + s[1])

def do_symlink():
    if system() == "Windows":
        return
    
    for s in vars.TO_SYMLINK:
        if not path.isfile(vars.INSTALL_PATH + s[1]):
            os.symlink(vars.INSTALL_PATH + s[0], vars.INSTALL_PATH + s[1])

def install():
    lastver = versions.get_version_list()["versions"][-1]

    free_space_check(lastver["presz"], lastver["postsz"])
    prepare_symlink()

    gui.message(_("Getting the archive..."), 0)
    download_extract(vars.SOURCE_URL + lastver["url"], lastver["file"], vars.INSTALL_PATH)

    do_symlink()

def update():
    """
    The simplest part of all this - if this function is called, we know the user wants to update.
    """

    presz = 0
    postsz = 0
    for patch in versions.get_patch_chain():
        presz += patch["presz"]
        postsz += patch["postsz"]

    # check if it is more efficient to download the game or the patches
    lastver = versions.get_version_list()["versions"][-1]

    if "presz" in lastver and lastver["presz"] < presz: # this means the patches are heavier than the bare download
        install()
        return

    free_space_check(presz, postsz)
    prepare_symlink()

    gui.message(_N("Getting %s patch...", "Getting %s patches...", len(versions.get_patch_chain())) % len(versions.get_patch_chain()), 0)

    for patch in versions.get_patch_chain():
        gui.message(_("Downloading patch %s to %s...") % (patch["from"], patch["to"]), 1)
        download_extract(vars.SOURCE_URL + patch["url"], patch["file"], vars.INSTALL_PATH)
    
    do_symlink()
