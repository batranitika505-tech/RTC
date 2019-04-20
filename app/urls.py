from django.urls import path
from . import views


urlpatterns = [
    path('obstacle', views.ObstacleView.as_view()),
    path('crack', views.CrackView.as_view()),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
]
