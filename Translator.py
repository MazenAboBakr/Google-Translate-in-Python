# Made By Mazen AboBakr 12/15/2022
# Google Translate in Python 

from googletrans import Translator, constants
from pprint import pprint
translator = Translator()

# Translate to French
translation = translator.translate("Hello World", dest="fr")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
