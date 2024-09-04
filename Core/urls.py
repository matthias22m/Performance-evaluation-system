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
    path('activities/add/', views.add_activity, name='add_activity'),
    path('activities/edit/<int:id>/', views.edit_activity, name='edit_activity'),
    path('activities/delete/<int:id>/', views.delete_activity, name='delete_activity'), 
    path('subactivity_create/', views.subactivity_create, name='create_subactivity'),
    path('subactivity_list/', views.subactivity_list, name='subactivity_list'),
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail')
]



