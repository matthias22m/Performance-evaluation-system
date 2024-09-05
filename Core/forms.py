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