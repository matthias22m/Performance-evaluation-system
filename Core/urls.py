from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.index,name='index'), 
    path('profile/',views.profile,name='profile'),
    path('activities/',views.activities,name='activities'),
    path('evaluation/',views.evaluation,name='evaluation'),
    path('unit_create/', views.unit_create, name='create_unit'),
    path('unit_list/', views.unit_list, name='unit_list'),
    path('detail_unit/<int:pk>',views.detail_unit ,name='detail_unit'),
    path('plan_create/', views.plan_create, name='create_plan'),
    path('plan_list/', views.plan_list, name='plan_list'),
    path('detail_plan/<int:pk>',views.detail_plan ,name='detail_plan'),
]