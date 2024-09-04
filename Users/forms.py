from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

Employee = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-input',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input',
    }))

class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = Employee
        fields = ['first_name','last_name','position','email','phone_number','job_title','salary','password1','password2']
