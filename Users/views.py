from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EmployeeRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Employee, Profile, Group
from Core.models import CharacterEvaluation, SubActivity


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

    evaluations = CharacterEvaluation.objects.get(id = user.id)
    total_evaluation = evaluations.behavior_one + evaluations.behavior_two + evaluations.behavior_three + evaluations.behavior_four + evaluations.behavior_five + evaluations.behavior_six
    context = {
        "target_employee": target_employee,
        "employee_image":employee_image,
        "employee_group":employee_group,
        "total_evaluation":total_evaluation,
        "employees":employee_group.employee.all(),
        "recent_activities":recent_activities
    }
    return render(request, 'Users/homePage.html', context)

