from django.urls import path

from . import views

urlpatterns = [
    path('subactivity_create/', views.subactivity_create, name='create_subactivity'),
    path('subactivity_list/', views.subactivity_list, name='subactivity_list')
]