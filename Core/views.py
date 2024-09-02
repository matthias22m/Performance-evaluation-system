from django.shortcuts import render



def profile(request):
    return render(request,'employee-profile.html')
    
def activities(request):
    return render(request,'activities.html')


def evaluation(request):
    return render(request,'evaluation.html')

def char_evaluation(request):
    return render(request,'char_evaluation.html')

def leader_page(request):
    return render(request,'leader_page.html')
