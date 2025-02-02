# from django import forms

# class FAQForm(forms.Form):
#     answer = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'ckeditor',
#         'script_id': 'answer-editor'  # Ensure this is added
#     }))
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget  

from .models import FAQ

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditor5Widget(attrs={'script_id': 'faq_editor'}))

    class Meta:
        model = FAQ
        fields = ['answer']

