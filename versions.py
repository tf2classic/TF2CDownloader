from os import path
from subprocess import run
from platform import system
from gettext import gettext as _
from gettext import ngettext as _N
import httpx
import gui
import vars
import json

VERSION_LIST = None
PATCH_CHAIN = None

def get_version_list():
    global VERSION_LIST
    if VERSION_LIST is None:
        try:
            VERSION_JSON = httpx.get(vars.SOURCE_URL + 'versions.json')
            VERSION_LIST = json.loads(VERSION_JSON.text)
        except httpx.RequestError:
            gui.message_end(_("Could not get version list. If your internet connection is fine, the servers could be having technical issues."), 1)
    return VERSION_LIST

def update_version_file():
    """
    The previous launcher/updater leaves behind a rev.txt file with the old internal revision number.
    To avoid file bloat, we reuse this, but replace it with the game's semantic version number.
    To obtain the game's semantic version number, we do some horrible parsing of the game's version.txt
    file, which is what the game itself uses directly to show the version number on the main menu, etc.
    """
    try:
        old_version_file = open(vars.INSTALL_PATH + '/tf2classic/version.txt', 'r')
    except FileNotFoundError:
        if gui.message_yes_no(_("We can't read the version of your installation. It could be corrupted. Do you want to reinstall the game?"), False):
            return False
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)
    old_version = old_version_file.readlines()[1]
    before, sep, after = old_version.partition('=')
    if len(after) > 0:
        old_version = after
    old_version = old_version.replace('.', '')
    new_version_file = open(vars.INSTALL_PATH + '/tf2classic/rev.txt', 'w')
    # We unconditionally overwrite rev.txt since version.txt is the canonical file.
    new_version_file.write(old_version)
    new_version_file.close()
    old_version_file.close()
    return True

def patch_chain(ver_from, ver_to):
    current_version = ver_from
    global PATCH_CHAIN
    PATCH_CHAIN = []
    while current_version != ver_to:
        if not current_version in VERSION_LIST["patches"]:
            # still not in the latest version, could not find patch
            return False
        patch = VERSION_LIST["patches"][current_version]
        patch["from"] = current_version
        if "file" not in patch:
            patch["file"] = patch["url"]
        if patch in PATCH_CHAIN:
            # somehow managed to get ourselves into a loop, avoid the memory hogging infinite loop, killer of desktops
            return False
        PATCH_CHAIN.append(patch)
        current_version = patch["to"]
    return True

def get_patch_chain():
    global PATCH_CHAIN
    return PATCH_CHAIN

def check_for_updates():
    """
    It's all math here. We can compare the version number against remote variables to see what we should do.
    """

    # This probably was already communicated to the user in update_version_file(), but if version.txt doesn't exist, skip updating.
    if not path.exists(vars.INSTALL_PATH + '/tf2classic/version.txt'):
        return 'reinstall'

    try:
        local_version_file = open(vars.INSTALL_PATH + '/tf2classic/rev.txt', 'r')
        local_version = local_version_file.read().rstrip('\n')
    except ValueError:
        if gui.message_yes_no(_("We can't read the version of your installation. It could be corrupted. Do you want to reinstall the game?"), False):
            return 'reinstall'
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)

    found = False
    for ver in get_version_list()["versions"]:
        if ver["ver"] == local_version:
            found = True
            break
    
    if not found:
        if gui.message_yes_no(_("The version of your installation is unknown. It could be corrupted. Do you want to reinstall the game?"), False):
            return 'reinstall'
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)

    latest_version = VERSION_LIST["versions"][-1]["ver"]

    if local_version == latest_version:
        if gui.message_yes_no(_("We think we've found an existing up-to-date installation of the game. Do you want to reinstall it?"), False):
            return 'reinstall'
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)
    if patch_chain(local_version, latest_version):
        if gui.message_yes_no(_("An update is available for your game. Do you want to install it?"), None, True):
            return 'update'
        else:
            if gui.message_yes_no(_("In that case, do you want to reinstall completely?"), 0):
                return 'reinstall'
            else:
                gui.message_end(_("We have nothing to do. Goodbye!"), 0)
    else:
        # We did not find an applicable patch chain to properly update the game, forcing us to relie on the ol' reinstallation method.
        if gui.message_yes_no(_("An update is available for your game. Do you want to install it?"), None, True):
            return 'reinstall'
        else:
            gui.message_end(_("We have nothing to do. Goodbye!"), 0)
