from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),    
    path('activities/', views.activities, name='activities'),
    path('employee/', views.employee, name='employee'),      
    path('evaluation/', views.evaluation, name='evaluation'),
    path('logout/', views.logout_view, name='logout'),   
    path('activities/add/', views.add_activity, name='add_activity'),
    
]