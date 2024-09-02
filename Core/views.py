from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubActivity
from .forms import SubActivityForm
# Create your views here.

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