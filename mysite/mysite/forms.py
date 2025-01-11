from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length= 50)
    email = forms.EmailField(required=True, validators=[EmailValidator()])
    message = forms.CharField(required=True, max_length= 1000, widget= forms.Textarea)