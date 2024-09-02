from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def activities(request):
    return render(request, 'core/activities.html')

def employee(request):
    return render(request, 'core/employee.html')

def evaluation(request):
    return render(request, 'core/evaluation.html')

def logout_view(request):
    return render(request, 'core/logout.html')