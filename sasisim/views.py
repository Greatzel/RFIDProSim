from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def sasi(request):
    return render(request, 'sasisim/sasiview.html')


def submit():
    return HttpResponse('submission successful')
