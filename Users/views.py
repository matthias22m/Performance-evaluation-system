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


def EmployeeView(request):
    user = request.user
    target_employee = get_object_or_404(Employee, id=user.id)
    employee_image = Profile.objects.filter(id = user.id).first()
    recent_activities = SubActivity.objects.filter(employee=target_employee).values()
    employee_group = target_employee.group.all().first()
    activities=SubActivity.objects.all()

    evaluations = CharacterEvaluation.objects.filter(id=user.id).values()
    avr, sum = 0,0
    for i in evaluations:
        avr += 1
        sum += i['result']
        print(i['result'])
        print(sum)

    context = {
        "target_employee": target_employee,
        "employee_image":employee_image,
        "employee_group":employee_group,
        # "total_evaluation":total_evaluation,
        "employees":employee_group.employee.all(),
        'activities':activities
        
    }
    return render(request, 'Users/homePage.html', context)



def list_activities(request):
    activities=SubActivity.objects.all()
    
    return render(request,'Users/activitiesPage.html',{'activities':activities})



def Evaluation(request):
    
    user = request.user
    
    target_employee = get_object_or_404(Employee, id=user.id)
    characterEvaluation=CharacterEvaluation.objects.all()
    employee_group = target_employee.group.all().first()
    contexts={"employees":employee_group.employee.all()}

    
    if request.method=='POST':
        evaluated_id=int(request.POST.get("selection"))
        
        if evaluated_id==user.id:
            evaluated_user_id=user.id
            percent=5
        else:
            evaluated_user_id=get_object_or_404(Employee, id=evaluated_id).id
            percent=15
            
        first_result=(percent*float(request.POST.get('first_list'))*25)/400
        second_result=(percent*float(request.POST.get('second_list'))*20)/400
        third_result=(percent*float(request.POST.get('third_list'))*15)/400
        fourth_result=(percent*float(request.POST.get('fourth_list'))*15)/400
        fifth_result=(percent*float(request.POST.get('fifth_list'))*15)/400
        sixth_result=(percent*float(request.POST.get('sixth_list'))*10)/400
        total=first_result+second_result+third_result+fourth_result+fifth_result+sixth_result
        
        
        evaluation = CharacterEvaluation(
            employee=target_employee,
            evaluator=get_object_or_404(Employee, id=evaluated_user_id),
            evaluation_date=date.today(),  # Set the current date as the evaluation date
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