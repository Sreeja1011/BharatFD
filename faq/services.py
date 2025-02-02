from googletrans import Translator
from django.conf import settings

translator = Translator()

def translate_text(text: str, dest: str) -> str:
    try:
        result = translator.translate(text, dest=dest)
        return result.text
    except Exception as e:
        return text

