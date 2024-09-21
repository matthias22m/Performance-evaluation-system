from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import SubActivity,CharacterEvaluation
from .forms import SubActivityForm, EmployeeForm
from django.contrib.auth import get_user_model
from django import forms
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .decorators import position_required
from Users.views import EmployeeView
from Users.models import Group
from .models import SubActivity
from .forms import SubActivityForm
from .models import Unit
from .forms import UnitForm
from .models import Plan
from .forms import PlanForm

@login_required
def home(request):
    if request.user.unit == None:
        return EmployeeView(request)
    annual_plan = request.user.unit.plans.first().annual_plans.first()
    casual_plan = request.user.unit.plans.first().casual_plans.first()
    
    employee = request.user
    employees = request.user.unit.employees.exclude(email__in=[request.user.email]).order_by('first_name','last_name')[:2]
    context = {'employee':employee, 'employees':employees, 'annual_plan':annual_plan,'casual_plan':casual_plan}
    
    return render(request,'core/home.html',context)

@position_required
def groups(request):
    groups = request.user.unit.groups.all()
    employees = request.user.unit.employees.exclude(email__in=[request.user.email])
    if request.method == 'POST':
        employee = request.POST.getlist('employees[]')
        group_name = request.POST.get('group_name')
        unit = request.user.unit
        
        group = Group.objects.create(
            unit=unit,
            name=group_name
        )
        group.employee.set(employee)
        group.save()
        
        return redirect('groups')


    context = {'groups':groups,'employees':employees}
    return render(request, 'core/groups.html', context)

@position_required
def all_plans(request):
    annual_plans = request.user.unit.plans.first().annual_plans.all()
    casual_plans = request.user.unit.plans.first().casual_plans.all()
    
    context = {'annual_plans':annual_plans,'casual_plans':casual_plans}
    
    return render(request, 'core/plan.html',context)

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


def unit_create(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'unit_created successfully.')
            return redirect('create_unit')
    else:
        form = UnitForm()
    return render(request, 'Core/create_unit.html', {'form':form})

def unit_list(request):
    unit = Unit.objects.all()

    context = {'unit':unit}

    return render(request, 'Core/unit_list.html', context)

def detail_unit(request,pk):
    unit=Unit.objects.get(id=pk)
    context={'unit':unit}
    return render(request,'Core/detail_unit.html',context=context)

def plan_create(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'plan_created successfully.')
            return redirect('create_plan')
    else:
        form = PlanForm()
    return render(request, 'Core/create_plan.html', {'form':form})

def plan_list(request):
    plan = Plan.objects.all()
    context = {'plan':plan}
    return render(request, 'Core/plan_list.html', context)

def detail_plan(request,pk):
    plan=Plan.objects.get(id=pk)
    context={'plan':plan}
    return render(request,'Core/detail_plan.html',context=context)
