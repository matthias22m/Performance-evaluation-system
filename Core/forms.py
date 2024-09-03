from django import forms
from .models import SubActivity, Unit

from django.contrib.auth import get_user_model

Employee = get_user_model()

class SubActivityForm(forms.ModelForm):
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(),widget=forms.Select(attrs={
        'class': 'activity-unit',
    }))
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(),widget=forms.Select(attrs={
        'class': 'activity-employee',
    }))
    deadline = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'activity-deadline',
    }))
    activity = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'activity-description',
    }))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'activity-weight',
    }))
    
    class Meta:
        model = SubActivity
        fields = ['unit', 'employee', 'deadline', 'activity', 'weight']
        
class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'first-name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'last-name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
    }))
    salary = forms.DecimalField(widget=forms.NumberInput(attrs={
        'id': 'salary',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'phone-number',
    }))
    job_title = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'job-title',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
    }))
    
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name','unit', 'email','salary','phone_number', 'job_title']
        
    def save(self, commit=True):
        employee = super().save(commit=False)
        employee.set_password(self.cleaned_data["password"])
        if commit:
            employee.save()
        return employee
