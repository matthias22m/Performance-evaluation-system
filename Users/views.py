from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeRegisterForm
from django.contrib.auth.decorators import login_required

from .models import Employee, Profile, Group
from Core.models import CharacterEvaluation



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
    target_employee = Employee.objects.get(id = user.id)
    employee_image = Profile.objects.get(id = user.id)
    employee_group = Group.objects.get(id = user.id)
    evaluations = CharacterEvaluation.objects.get(id = user.id)
    total_evaluation = evaluations.behavior_one + evaluations.behavior_two + evaluations.behavior_three + evaluations.behavior_four + evaluations.behavior_five + evaluations.behavior_six
    context = {
        "target_employee": target_employee,
        "employee_image":employee_image,
        "employee_group":employee_group,
        "total_evaluation":total_evaluation
    }
    return render(request, 'Users/example.html', context)

