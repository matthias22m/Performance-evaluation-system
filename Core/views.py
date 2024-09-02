from django.shortcuts import render
from django.shortcuts import render, redirect
from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'deadline', 'description')

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities_list')
    else:
        form = ActivityForm()
    return render(request, 'activities/add_activity.html', {'form': form})

def activities_list(request):
    activities = Activity.objects.all()
    return render(request, 'activities/list.html', {'activities': activities})

def index(request):
    return render(request, 'core/index.html')

def activities(request):
    return render(request, 'core/activities.html')

def employee(request):
    return render(request, 'core/employee.html')

def evaluation(request):
    return render(request, 'core/evaluation.html')

def logout_view(request):
    return render(request, 'core/logout.html')
