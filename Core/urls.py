from django.urls import path

from . import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('units/', views.units, name='units'),
    path('plan/', views.plan, name='plan'),
    # path('logout/', views.logout, name='logout'),
]
