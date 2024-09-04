from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeRegisterForm
from django.contrib.auth.decorators import login_required



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
