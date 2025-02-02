from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget  

from .models import FAQ

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditor5Widget(attrs={'script_id': 'faq_editor'}))

    class Meta:
        model = FAQ
        fields = ['answer']

