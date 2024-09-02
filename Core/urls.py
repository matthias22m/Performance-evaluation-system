from django.urls import path

from . import views

urlpatterns = [ 
     
    path('profile/',views.profile,name='profile'),
<<<<<<< HEAD
    path('activities',views.activities,name='activities'),
    path('evaluation',views.evaluation,name='evaluation'),
    path('char_evaluation',views.char_evaluation,name='char_evaluation'),
    path('leader',views.leader_page,name='leader_page')
=======
    path('activities/',views.activities,name='activities'),
     path('evaluation/',views.evaluation,name='evaluation')
>>>>>>> e21a06b4fb34ed7e9d8213ee639c29524eaf046d
]