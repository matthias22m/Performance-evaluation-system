from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),    
    path('activities/', views.activities, name='activities'),
    path('employee/', views.employee, name='employee'),      
    path('evaluation/', views.evaluation, name='evaluation'),
    path('employee/', views.employee, name='employee'),
    path('groups/', views.groups,name='groups'),
    path('logout/', views.logout_view, name='logout'),   
    # path('activities/add/', views.add_activity, name='add_activity'),
    path('subactivity/edit/<int:id>/', views.edit_subactivity, name='edit_subactivity'),
    path('subactivity/delete/<int:id>/', views.delete_subactivity, name='delete_subactivity'), 
    path('subactivity/', views.subactivity_view, name='subactivity'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail')
]



