fr = {
    "running_background": "On dirait qu'on est en train de tourner en arrière plan. On ne veut pas ça, donc on sort.",

    "exception_line": "[italic magenta]----- Détails des exceptions au dessus de cette ligne -----",
    "exception": "[bold red]:warning: Le programme a échoué. Postez un screenshot dans #technical-issues sur le Discord (en anglais seulement). :warning:[/bold red]",
    "exit_safe": "[bold]Vous pouvez fermer cette fenêtre.",
    "exit": "Appuyez sur Entrée pour sortir.",

    "prompt_valid": {"yes": True, "y": True, "no": False, "oui": True, "o": True, "non": False, "n": False}, # all possible choices (yes or no)
    "prompt_prompt": {None: " {o/n}", "y": " {O/n}", "n": " {o/N}"}, # only replace the "{y/n}" parts. uppercase means "by default"
    "prompt_invalid": "[bold blue]Répondez avec 'oui' ou 'non' ('o' ou 'n').[/bold blue]",

    "setup_found": "Le dossier sourcemods a été automatiquement trouvé ici : %s",
    "setup_found_question": "C'est l'endroit d'installation recommendé. Voulez-vous installer TF2 Classic ici ?",
    "setup_not_found": "ATTENTION : Le dossier sourcemods de Steam n'a pas été trouvé, ou alors vous avez choisi de ne pas l'utiliser.",
    "setup_not_found_question": "Voulez-vous l'extraire dans %s ? Vous devez ensuite le déplacer dans votre dossier sourcemods manuellement.",
    "setup_input": "Veuillez entrez l'emplacement du dossier où va être installer TF2 Classic.\n",
    "setup_accept": "TF2 Classic va être installer ici : %s\nEs-ce que vous acceptez ?",
    "setup_reset": "Réinitialisation...\n",

    "setup_missing_aria2": "Vous devez installer Aria2 pour utiliser ce script.",
    "setup_missing_zstd": "Vous devez installer Zstd pour utiliser ce script.",

    "free_space_download": "Vous n'avez pas assez d'espace libre pour télécharger TF2 Classic. Vous devez avoir 4.5GO de libre au minimum sur votre disque dur principale.",
    "free_space_extract": "Vous n'avez pas assez d'espace libre pour extraire TF2 Classic. Vous devez avoir 12GO de libre au minimum sur l'emplacement d'installation.",
    "location_doesnt_exist": "L'emplacement d'extraction spécifié n'existe pas.",

    "starting_download": "Téléchargement de TF2 Classic... Vous pouvez voir certaines erreurs qui peuvent être parfaitement ignorées.",
    "starting_extract": "Extraction de l'archive téléchargée, veuillez patentier.",

    "troubleshoot_blacklist": "Application de la liste noir de sécurité...",
    "troubleshoot_blacklist_fail": "ATTENTION : impossible d'appliquer la liste noir de sécurité.",

    "success": "L'installation est terminée. N'oubliez pas de redémarrer Steam !",
}