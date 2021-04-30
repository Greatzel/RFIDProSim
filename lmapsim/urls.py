from django.urls import path
from . import views
from ProSim.views import sasi
from django.contrib import admin

urlpatterns = [
    path('test1/', views.index),
    path('lmap/', views.lmap, name='lmap'),
    path('submit', views.submit, name='submit'),
    path('sasi/', sasi, name='sasi'),
    path('', views.home, name='home'),
]
