from django.shortcuts import render
from django.http import HttpResponse
from lmapsim.models import Lmap
from django.template import loader
from django.http import JsonResponse


def home(request):
    return render(request, 'homepage.html')


def lmap(request):
    return render(request, 'lmapsim/lmapview.html')


def sasi(request):
    print("rciasim urls.py sasi request")
    return render(request, 'sasisim/sasiview.html')


def rcia(request):
    return render(request, 'rciasim/rciaview.html')
