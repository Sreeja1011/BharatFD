from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from .services import translate_text

class FAQ(models.Model):
    # Default fields (English)
    question = models.TextField(help_text="Default question in English.")
    answer = RichTextField(help_text="Answer with rich text formatting.")

    question_hi = models.TextField(blank=True, null=True, help_text="Question in Hindi")
    question_bn = models.TextField(blank=True, null=True, help_text="Question in Bengali")

    def get_translated_question(self, lang: str = "en") -> str:
        """Return the translated question for the requested language."""
        if lang == "en":
            return self.question

        # Attempt to use the pre-generated field if available
        field_name = f"question_{lang}"
        translated = getattr(self, field_name, None)
        if translated:
            return translated

        # Otherwise, try to fetch from cache or generate dynamically.
        cache_key = f"faq:{self.pk}:question:{lang}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        # Generate a dynamic translation.
        translated = translate_text(self.question, dest=lang)
        cache.set(cache_key, translated, timeout=86400)  # Cache for 1 day
        return translated

    def __str__(self):
        return self.question
