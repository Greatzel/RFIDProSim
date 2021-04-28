from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('test1/', views.index),
    path('lmap/', views.lmap),
    path('submit/', views.submit, name='submit'),
]