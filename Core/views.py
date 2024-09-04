from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import SubActivity
from .forms import SubActivityForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Activity
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .decorators import position_required

# def activity_list(request):
#     activities = Activity.objects.all()
#     return render(request, 'your_template.html', {'activities': activities})

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'deadline', 'description')

# @require_POST
# def add_activity(request):
#     activity_name = request.POST.get('activity_name')
#     description = request.POST.get('description')
#     deadline = request.POST.get('deadline')
#     assigned_person = request.POST.get('assign_person')

#     Activity.objects.create(
#         name=activity_name,
#         description=description,
#         deadline=deadline,
#         assigned_person=assigned_person
#     )
#     return redirect('activity_list')

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
def groups(request):
    return render(request, 'core/groups.html')

Employee = get_user_model()

@position_required
def subactivity_view(request):
    subactivities = SubActivity.objects.all()
    unit = request.user.unit
    employees = None
    if unit is not None:
        employees = unit.employees.exclude(email__in=[request.user.email])

    
    if request.method == 'POST':
        form = SubActivityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Activity assigned successfully.')
            return redirect('subactivity')
    else:
        form = SubActivityForm()
    context = {'subactivities':subactivities,'employees':employees,'form':form, 'unit':unit}
    return render(request, 'Core/activities.html', context)

def edit_subactivity(request, id):
    subactivity = get_object_or_404(SubActivity,id=id)
    unit = request.user.unit
    employees = None
    if unit is not None:
        employees = unit.employees.exclude(email__in=[request.user.email])

    
    if request.method == 'POST':
        form = SubActivityForm(request.POST,instance=subactivity)
        if form.is_valid():
            form.save()
            messages.success(request, f'Activity updated successfully.')
            return redirect('subactivity')
    else:
        form = SubActivityForm(instance=subactivity)
    context = {'subactivity':subactivity,'employees':employees,'form':form, 'unit':unit}
    return render(request, 'Core/edit_activity.html', context)

def delete_subactivity(request, id):
    activity = get_object_or_404(SubActivity, id=id)
    activity.delete()

#LIST AND DETAL FOR EMPLOYEES
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})
    return redirect('subactivity')