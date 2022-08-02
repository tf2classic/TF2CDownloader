import vars
import gui
import urllib.request

def apply_blacklist():
    gui.message(_("Applying safety blacklist..."))
    try:
        urllib.request.urlretrieve("https://wiki.tf2classic.com/serverlist/blacklist.php", vars.INSTALL_PATH + "/tf2classic/cfg/server_blacklist.txt")
    except:
        gui.message(_("WARNING: could not apply safety blacklist."))
