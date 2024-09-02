from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),               # Home page
    path('activities/', views.activities, name='activities'),  # Activities page
    path('employee/', views.employee, name='employee'),      # Employee page
    path('evaluation/', views.evaluation, name='evaluation'),  # Evaluation page
    path('logout/', views.logout_view, name='logout'),      # Logout page
]