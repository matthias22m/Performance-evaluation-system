from django import forms
from .models import SubActivity
from .models import Unit
from .models import Plan

class SubActivityForm(forms.ModelForm):
    class Meta:
        model = SubActivity
        fields = ['unit', 'employee', 'deadline', 'activity', 'weight']
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'unit_leader', 'work_unit']
class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['work_unit', 'unit']