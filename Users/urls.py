from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
from . import views

urlpatterns = [ 
    path("register/", views.register, name="user_register"),
    path("login/", auth_views.LoginView.as_view(template_name= 'users/login.html', authentication_form=CustomLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name="logout"),              
    path('profile/', views.EmployeeView, name = 'profile') ,
    path('activities/',views.list_activities,name='activities') ,
    path('evaluation/',views.Evaluation,name='user-evaluation')          
    path('',views.user),   
]
