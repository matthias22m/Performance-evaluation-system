from django.shortcuts import render

def user(request):
    return render(request,'Users/user.html')
