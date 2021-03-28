from django import forms
from forum.models import Replie

class ReplieForm(forms.Form):
    text = forms.CharField(label="Text", help_text="Text of teste")
    owner = forms.CharField(label="User", help_text="Your name")
