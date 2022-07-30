en = {
    "running_background": "Looks like we're running in the background. We don't want that, so we're exiting.",

    "exception_line": "[italic magenta]----- Exception details above this line -----",
    "exception": "[bold red]:warning: The program has failed. Post a screenshot in #technical-issues on the Discord. :warning:[/bold red]",
    "exit_safe": "[bold]You are safe to close this window.",
    "exit": "Press Enter to exit.",

    "prompt_valid": {"yes": True, "y": True, "no": False, "n": False}, # all possible choices (yes or no)
    "prompt_prompt": {None: " {y/n}", "y": " {Y/n}", "n": " {y/N}"}, # only replace the "{y/n}" parts. uppercase means "by default"
    "prompt_invalid": "[bold blue]Please respond with 'yes' or 'no' (or 'y' or 'n').[/bold blue]",

    "setup_found": "Sourcemods folder was automatically found at: %s",
    "setup_found_question": "It's the recommended installation location. Would you like to install TF2 Classic there?",
    "setup_not_found": "WARNING: Steam's sourcemods folder has not been found, or you chose not to use it.",
    "setup_not_found_question": "Would you like to extract in %s? You must move it to your sourcemods manually.",
    "setup_input": "Please, enter the location in which TF2 Classic will be installed to.\n",
    "setup_accept": "TF2 Classic will be installed in %s\nDo you accept?",
    "setup_reset": "Reinitialising...\n",

    "setup_missing_aria2": "You need to install Aria2 to use this script.",
    "setup_missing_zstd": "You need to install Zstd to use this script.",

    "free_space_download": "You don't have enough free space to download TF2 Classic. A minimum of 4.5GB on your primary drive is required.",
    "free_space_extract": "You don't have enough free space to extract TF2 Classic. A minimum of 12GB at your chosen extraction site is required.",
    "location_doesnt_exist": "The specified extraction location does not exist.",

    "starting_download": "Starting the download for TF2 Classic... You may see some errors that are safe to ignore.",
    "starting_extract": "Extracting the downloaded archive, please wait patiently.",

    "troubleshoot_blacklist": "Applying safety blacklist...",
    "troubleshoot_blacklist_fail": "WARNING: could not apply safety blacklist.",

    "success": "The installation has successfully completed. Remember to restart Steam!",
}