from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import SubActivity,CharacterEvaluation
from .forms import SubActivityForm, EmployeeForm
from django.contrib.auth import get_user_model
from django import forms
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .decorators import position_required

# def activity_list(request):
#     activities = Activity.objects.all()
#     return render(request, 'your_template.html', {'activities': activities})

# class ActivityForm(forms.ModelForm):
#     class Meta:
#         model = Activity
#         fields = ('name', 'deadline', 'description')

# @require_POST
# def add_activity(request):
#     activity_name = request.POST.get('activity_name')
#     description = request.POST.get('description')
#     deadline = request.POST.get('deadline')
#     assigned_person = request.POST.get('assign_person')

   # Activity.objects.create(
    #    name=activity_name,
    #    description=description,
     #   deadline=deadline,
     #   assigned_person=assigned_person
   # )
    #return redirect('activity_list')
def home(request):
    return render(request,'core/home.html')
#     Activity.objects.create(
#         name=activity_name,
#         description=description,
#         deadline=deadline,
#         assigned_person=assigned_person
#     )
#     return redirect('activity_list')

# def activities_list(request):
#     activities = Activity.objects.all()
#     return render(request, 'activities/list.html', {'activities': activities})

def activities(request):
    return render(request, 'core/activities.html')

def employee(request):
    return render(request, 'core/employee.html')


def logout_view(request):
    return render(request, 'core/logout.html')
def employee(request):
    return render(request, 'core/employee.html')
def groups(request):
    return render(request, 'core/groups.html')
def all_plans(request):
    return render(request, 'core/plan.html')

def all_employees(request):
    return render(request, 'core/all-employ.html') 
def add_employee(request):
    return render(request, 'core/add_emp.html')


Employee = get_user_model()

@position_required
def subactivity_view(request):
    unit = request.user.unit
    subactivities = None
    employees = None
    if unit is not None:
        subactivities = SubActivity.objects.filter(unit=unit)
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

@position_required
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

@position_required
def delete_subactivity(request, id):
    activity = get_object_or_404(SubActivity, id=id)
    activity.delete()
    return redirect('subactivity')
    
@position_required
def evaluation_view(request):
    evaluations = CharacterEvaluation.objects.all()
    unit = request.user.unit
    employees = None
    if unit is not None:
        employees = unit.employees.exclude(email__in=[request.user.email])
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = Employee.objects.get(id=employee_id)
        behavior_one = request.POST.get('behavior1_score')
        behavior_two = request.POST.get('behavior2_score')
        behavior_three = request.POST.get('behavior3_score')
        behavior_four = request.POST.get('behavior4_score')
        behavior_five = request.POST.get('behavior5_score')
        behavior_six = request.POST.get('behavior6_score')
        result = float(behavior_one)+float(behavior_two)+float(behavior_three)+float(behavior_four)+float(behavior_five)+float(behavior_six)

        CharacterEvaluation.objects.create(
            employee = employee,
            evaluator = request.user,
            behavior_one = behavior_one,
            behavior_two = behavior_two,
            behavior_three = behavior_three,
            behavior_four = behavior_four,
            behavior_five = behavior_five,
            behavior_six = behavior_six,
            result= result
        )
        return redirect('evaluation')
    context = {'employees':employees,'evaluations':evaluations}
    return render(request, 'core/evaluation.html',context)

#LIST AND DETAL FOR EMPLOYEES
@position_required
def employee_view(request):
    unit = request.user.unit
    employees = None
    if unit is not None:
        employees = unit.employees.exclude(email__in=[request.user.email])
        
    context = {'employees': employees,}
    return render(request, 'core/employee.html', context)

@position_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.unit = request.user.unit
            employee.save()
            messages.success(request, f'Employee created successfully.')
            return redirect('employees')
    else:
        form = EmployeeForm()   
    
    return render(request, 'core/add_emp.html')