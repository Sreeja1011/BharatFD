from django.contrib import admin

# Register your models here.
from .models import FAQ
from ckeditor.fields import RichTextField
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "question_hi", "question_bn")
    search_fields = ("question", "question_hi", "question_bn")
    list_filter = ("question",)

    # Optionally, customize the form to use CKEditor for the answer field
    # This is automatically handled if your ckeditor widget is set in settings.
