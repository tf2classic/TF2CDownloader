import locale

from langs.en import en
from langs.es import es
from langs.fr import fr
from langs.it import it
from langs.ru import ru

langs = {
    "en": en,
    "fr": fr,
    "es": es,
    "it": it,
    "ru": ru
}

lang = langs["en"]

locale = locale.getdefaultlocale()[0]
if locale in langs:
    lang.update(langs[locale])
elif locale.split("_")[0] in langs:
    lang.update(langs[locale.split("_")[0]])
