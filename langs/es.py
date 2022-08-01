es = {
    "running_background": "Parece que estamos corriendo en segundo plano. No queremos eso, así que vamos a salir",

    "exception_line": "[italic magenta]----- Detalles de la excepción arriba de esta línea -----",
    "exception": "[bold red]:warning: El programa ha fallado. Publique una captura de pantalla en #technical-issues en Discord (solo en inglés). :warning:[/bold red]",
    "exit_safe": "[bold]Puede cerrar esta ventana.",
    "exit": "Presiona Enter para salir.",

    "prompt_valid": {"yes": True, "y": True, "si": True, "sí": True, "s": True, "no": False, "n": False}, # all possible choices (yes or no)
    "prompt_prompt": {None: " {s/n}", "y": " {S/n}", "n": " {s/N}"}, # only replace the "{y/n}" parts. uppercase means "by default"
    "prompt_invalid": "[bold blue]Por favor, responda con 'sí' o 'no' (o 's' o 'n').[/bold blue]",

    "setup_found": "La carpeta Sourcemods se encontró automáticamente en: %s",
    "setup_found_question": "Es la ubicación de instalación recomendada. ¿Le gustaría instalar TF2 Classic allí?",
    "setup_not_found": "ADVERTENCIA: No se ha encontrado la carpeta sourcemods de Steam o usted decidió no usarla.",
    "setup_not_found_question": "¿Te gustaría extraer en %s? Debes moverlo a tus sourcemods manualmente.",
    "setup_input": "Por favor, ingrese la ubicación en la que se instalará TF2 Classic.\n",
    "setup_accept": "TF2 Classic se instalará en %s\n¿Aceptas?",
    "setup_reset": "Restableciendo...\n",

    "setup_missing_aria2": "Necesitas instalar Aria2 para usar este script.",
    "setup_missing_zstd": "Necesitas instalar Zstd para usar este script.",

    "free_space_download": "No tienes suficiente espacio libre para descargar TF2 Classic. Se requiere un mínimo de 4.5GB en tu disco principal.",
    "free_space_extract": "No tienes suficiente espacio libre para extraer TF2 Classic. Se requiere un mínimo de 12GB en el sitio de extracción elegido.",
    "location_doesnt_exist": "La ubicación de extracción especificada no existe.",

    "starting_download": "Iniciando la descarga de TF2 Classic... Es posible que veas algunos errores que puedes ignorar.",
    "starting_extract": "Extrayendo el archivo descargado, espere pacientemente.",

    "troubleshoot_blacklist": "Aplicando lista negra de seguridad…",
    "troubleshoot_blacklist_fail": "ADVERTENCIA: no se pudo aplicar la lista negra de seguridad.",

    "success": "La instalación se completó con éxito. ¡Recuerda reiniciar Steam!",
}