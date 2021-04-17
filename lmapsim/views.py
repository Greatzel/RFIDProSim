from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Test 1')

def lmap(request):
    return render(request, 'lmapsim/lmapview.html')