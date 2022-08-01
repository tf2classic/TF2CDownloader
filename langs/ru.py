en = {
    "running_background": "Похоже, что программа запущена в фоновом режиме. Выходим...",

    "exception_line": "[italic magenta]----- Детали об ошибке над этой линией -----",
    "exception": "[bold red]:warning: Программа выдала ошибку. Отправьте снимок экрана в #technical-issues в Discord-сервере TF2C. :warning:[/bold red]",
    "exit_safe": "[bold]Вы можете закрыть окно.",
    "exit": "Нажмите Enter для выхода.",
    
    "prompt_valid": {"да": True, "д": True, "yes": True, "y": True, "нет": False, "н": False, "no": False, "n": False}, # all possible choices (yes or no)
    "prompt_prompt": {None: " {д/н}", "y": " {Д/н}", "n": " {д/Н}"}, # only replace the "{y/n}" parts. uppercase means "by default"
    "prompt_invalid": "[bold blue]Пожалуйста, ответьте 'да' или 'нет' (или 'д'/'н').[/bold blue]",
    
    "setup_found": "Папка sourcemods была найдена в: %s",
    "setup_found_question": "Это рекомендуемое место установки. Вы хотите установить TF2 Classic туда?",
    "setup_not_found": "Предупреждение: папка sourcemods не была найдена, или вы решили выбрать место установки самостоятельно.",
    "setup_not_found_question": "Вы хотите распаковать игру в %s? Вам придётся переместить её в папку sourcemods вручную.",
    "setup_input": "Пожалуйста, укажите место установки игры.\n",
    "setup_accept": "TF2 Classic будет установлен в %s\nУстановить?",
    "setup_reset": "Перезапуск...\n",

    "setup_missing_aria2": "Вам нужно установить Aria2 для использования этой программы.",
    "setup_missing_zstd": "Вам нужно установить Zstd для использования этой программы.",

    "free_space_download": "У вас не хватает места для скачивания TF2 Classic. Необходимо минимум 4.5GB на вашем системном диске.",
    "free_space_extract": "У вас не хватает места для распаковки TF2 Classic. Необходимо минимум 12GB на выбраном диске.",
    "location_doesnt_exist": "Указаный путь не существует.",

    "starting_download": "Начинаем загрузку TF2 Classic... Вы можете увидеть ошибки, которые можно игнорировать.",
    "starting_extract": "Начинаем распаковку архива, пожалуйста подождите.",

    "troubleshoot_blacklist": "Применяем безопасный чёрный список...",
    "troubleshoot_blacklist_fail": "Предупреждение: чёрный список не был применён.",

    "success": "Установка успешно завершена. Не забудьте перезапустить Steam!",
}