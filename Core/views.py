from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import SubActivity
from .forms import SubActivityForm
from django.contrib.auth import get_user_model
# Create your views here.

Employee = get_user_model()

def subactivity_create(request):
    if request.method == 'POST':
        form = SubActivityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Activity assigned successfully.')
            return redirect('create_subactivity')
    else:
        form = SubActivityForm()
    return render(request, 'Core/create_subactivity.html', {'form':form})

def subactivity_list(request,pk):
    subactivities = SubActivity.objects.all()
    
    context = {'subactivities':subactivities}
    
    return render(request, 'Core/subactivities_list.html', context)

#LIST AND DETAL FOR EMPLOYEES
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})