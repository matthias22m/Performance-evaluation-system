from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'employee-profile.html')
    
def activities(request):
    return render(request,'activities.html')


def evaluation(request):
    return render(request,'evaluation.html')