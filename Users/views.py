from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EmployeeRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Employee, Profile, Group
from Core.models import CharacterEvaluation
from Core.models import SubActivity


def register(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created! You are now able to login now.')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def EmployeeView(request):
    user = request.user
    target_employee = get_object_or_404(Employee, id=user.id)
    employee_image = Profile.objects.get(employee = user.id)
    employee_group = target_employee.group.all().first()
    activities=SubActivity.objects.all()

    others_evaluations = CharacterEvaluation.objects.filter(employee=user.id).exclude(evaluator = user.id)
    own_evaluations = CharacterEvaluation.objects.filter(employee=user.id,evaluator = user.id)

    counter, sum = 0,0
    for i in others_evaluations:
        counter += 1
        sum += i.result
    try:
        others_evaluations_average = sum/counter
    except ZeroDivisionError:
        others_evaluations_average = 0
    
    employees = None
    if employee_group is not None:
        employees = employee_group.employee.all()

    context = {
        "target_employee": target_employee,
        "employee_image":employee_image,
        "employee_group":employee_group,
        "employees":employees,
        'activities':activities,
        "others_evaluations_average":others_evaluations_average,
        "own_evaluations":own_evaluations     
    }
    return render(request, 'Users/homePage.html', context)

@login_required
def list_activities(request):
    activities=SubActivity.objects.all()   
    return render(request,'Users/activitiesPage.html',{'activities':activities})

@login_required
def Evaluation(request):   
    user = request.user 
    employee_group = user.group.all().first()
    employees = None
    if employee_group is not None:
        employees = employee_group.employee.all()
        
    contexts={"employees":employees}

    if request.method=='POST':
        evaluated_id=int(request.POST.get("selection"))
        
        if evaluated_id==user.id:
            evaluated_user_id=user.id
            percent=5
        else:
            evaluated_user_id=evaluated_id
            percent=15
            
        first_result=(percent*float(request.POST.get('first_list'))*25)/400
        second_result=(percent*float(request.POST.get('second_list'))*20)/400
        third_result=(percent*float(request.POST.get('third_list'))*15)/400
        fourth_result=(percent*float(request.POST.get('fourth_list'))*15)/400
        fifth_result=(percent*float(request.POST.get('fifth_list'))*15)/400
        sixth_result=(percent*float(request.POST.get('sixth_list'))*10)/400
        total=first_result+second_result+third_result+fourth_result+fifth_result+sixth_result
        
        
        evaluation = CharacterEvaluation(
            employee=get_object_or_404(Employee, id=evaluated_user_id),
            evaluator=user,
            evaluation_date=date.today(),
            behavior_one=first_result,
            behavior_two=second_result,
            behavior_three=third_result,
            behavior_four=fourth_result,
            behavior_five=fifth_result,
            behavior_six=sixth_result,
            result=total
        )
        
        evaluation.save()
        
    return render(request,'Users/evaluationPage.html',contexts)
def user(request):
    return render(request,'Users/user.html')
