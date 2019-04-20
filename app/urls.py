from django.urls import path, include
from . import views


urlpatterns = [
    path('obstacle', views.ObstacleView.as_view()),
    path('crack', views.CrackView.as_view()),
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
]
