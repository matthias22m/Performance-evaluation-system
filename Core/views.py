from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubActivity
from .forms import SubActivityForm
from .models import Unit
from .forms import UnitForm
from .models import Plan
from .forms import PlanForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'employee-profile.html')
    
def activities(request):
    return render(request,'activities.html')


def evaluation(request):
    return render(request,'evaluation.html')

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
