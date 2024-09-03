from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django import forms
from .models import Activity
from django.views.decorators.http import require_POST

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'your_template.html', {'activities': activities})

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'deadline', 'description')
def edit_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    
    if request.method == 'POST':
        activity.name = request.POST.get('activity_name')
        activity.deadline = request.POST.get('deadline')
        activity.description = request.POST.get('description')
        activity.assigned_person = request.POST.get('assign_person')
        activity.save()
        return redirect('activities') 

    return render(request, 'edit_activity.html', {'activity': activity})
def delete_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    activity.delete()
    return redirect('activities')

@require_POST
def add_activity(request):
    activity_name = request.POST.get('activity_name')
    description = request.POST.get('description')
    deadline = request.POST.get('deadline')
    assigned_person = request.POST.get('assign_person')

    Activity.objects.create(
        name=activity_name,
        description=description,
        deadline=deadline,
        assigned_person=assigned_person
    )
    return redirect('activity_list')

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
def employee(request):
    return render(request, 'core/employee.html')
