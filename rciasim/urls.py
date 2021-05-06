from django.urls import path

import ProSim.views
from . import views
from ProSim.views import lmap
from django.contrib import admin

urlpatterns = [
    path('sasi', views.sasi, name='sasi'),
    path('lmap', lmap, name='lmap'),
    path('rciasubmit', views.rciasubmit, name='rciasubmit'),
    path('', ProSim.views.home, name='home'),
    # path('submitrcia', views.submitrcia, name='submitrcia')
]
