from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('evaluation/', views.evaluation_view, name='evaluation'),
    path('groups/', views.groups,name='groups'),
    path('subactivity/edit/<int:id>/', views.edit_subactivity, name='edit_subactivity'),
    path('subactivity/delete/<int:id>/', views.delete_subactivity, name='delete_subactivity'), 
    path('subactivity/', views.subactivity_view, name='subactivity'),
    path('plans/', views.all_plans, name='all_plans'), 
    path('employee/', views.employee_view, name='employees'),      
    path('employee/add/', views.employee_add, name='add_employee'),

    path('home/', views.home, name='home'),
    path('units/', views.units, name='units'),
    path('plan/', views.plan, name='plan'),
    # path('logout/', views.logout, name='logout'),
]
