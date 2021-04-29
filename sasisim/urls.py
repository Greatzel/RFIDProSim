from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('submit/', views.submit, name='submit'),
    path('sasi/', views.sasi, name='sasi'),
]