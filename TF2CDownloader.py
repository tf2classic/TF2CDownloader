from sys import stdin, exit
import vars
import gui
import setup
import install

# never used anywhere, should be deleted
#keepzip = False

def sanity_check():
	if not stdin or not stdin.isatty():
		print("Looks like we're running in the background. We don't want that, so we're exiting.")
		exit(1)

sanity_check()
setup.setup_path()
setup.setup_binaries()
install.tf2c_download()
install.tf2c_extract()

gui.message_end("Setup is over. Remember to restart Steam!", 0)
