from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-input',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input',
    }))
