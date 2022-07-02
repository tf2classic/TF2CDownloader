from langs.en import en
from langs.fr import fr
from langs.es import es
import locale

langs = {
    "en": en,
    "fr": fr,
    "es": es
}

lang = langs["en"]

locale = locale.getdefaultlocale()[0]
if locale in langs:
    lang.update(langs[locale])
elif locale.split("_")[0] in langs:
    lang.update(langs[locale.split("_")[0]])