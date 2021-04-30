from django.urls import path

import ProSim.views
from . import views
from ProSim.views import lmap
from django.contrib import admin

urlpatterns = [
    path('submitsasi', views.submitsasi, name='submitsasi'),
    path('sasi/', views.sasi, name='sasi'),
    path('lmap/', lmap, name='lmap'),
    path('', ProSim.views.home, name='home'),
]
