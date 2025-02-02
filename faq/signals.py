from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FAQ
from .services import translate_text

@receiver(post_save, sender=FAQ)
def generate_translations(sender, instance: FAQ, created, **kwargs):
    """
    Automatically generate translations for an FAQ after it's saved.
    This runs only if the translated fields are empty.
    """
    updated = False

    if not instance.question_hi:
        instance.question_hi = translate_text(instance.question, dest="hi")
        updated = True

    if not instance.question_bn:
        instance.question_bn = translate_text(instance.question, dest="bn")
        updated = True

    if updated:
        # Avoid recursion by updating only specific fields.
        instance.save(update_fields=["question_hi", "question_bn"])
