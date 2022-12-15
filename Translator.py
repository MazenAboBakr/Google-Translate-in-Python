from googletrans import Translator, constants
from pprint import pprint
translator = Translator()

translation = translator.translate("Hello World", dest="fr")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")