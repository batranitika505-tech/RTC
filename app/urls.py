from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('obstacle', views.ObstacleView.as_view()),
    path('crack', views.CrackView.as_view()),
    path('', views.index, name='index'),
    path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
]
