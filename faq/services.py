from googletrans import Translator
from django.conf import settings

translator = Translator()

def translate_text(text: str, dest: str) -> str:
    """
    Synchronously translate text using Google Translate.
    You can extend this function to support asynchronous tasks with Celery.
    """
    try:
        # Use googletrans to perform translation.
        result = translator.translate(text, dest=dest)
        return result.text
    except Exception as e:
        # Fallback: if translation fails, return the original text.
        return text

# Optional: Asynchronous translation using Celery
# Uncomment and adjust the following code if you want asynchronous translation.

# from celery import shared_task
#
# @shared_task
# def async_translate_text(text: str, dest: str) -> str:
#     try:
#         result = translator.translate(text, dest=dest)
#         return result.text
#     except Exception as e:
#         return text
#
# def translate_text(text: str, dest: str) -> str:
#     """
#     Dispatch an asynchronous task, or use the cached translation if available.
#     """
#     # For now, we call synchronously.
#     return async_translate_text.delay(text, dest).get(timeout=10)
