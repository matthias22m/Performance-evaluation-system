from django import forms
from .models import SubActivity

class SubActivityForm(forms.ModelForm):
    class Meta:
        model = SubActivity
        fields = ['unit', 'employee', 'deadline', 'activity', 'weight']