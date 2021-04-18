from django.urls import path
from . import views

urlpatterns = [
    path('test1/', views.index),
    path('lmap/', views.lmap),
    path('submit/', views.submit, name='submit')
]