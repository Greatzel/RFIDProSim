from django.shortcuts import render
from django.http import HttpResponse
from lmapsim.models import Lmap


# Create your views here.

def index(request):
    return HttpResponse('Test 1')


def lmap(request):
    return render(request, 'lmapsim/lmapview.html')


def submit(request):
    id_val = request.POST.get("lmapId")
    ids = request.POST.get("lmapIds")
    k1 = request.POST.get("lmapK1")
    k2 = request.POST.get("lmapK2")
    k3 = request.POST.get("lmapK3")
    k4 = request.POST.get("lmapK4")
    n1 = request.POST.get("lmapN1")
    n2 = request.POST.get("lmapN2")

    obj = Lmap(id_val, ids, k1, k2, k3, k4, n1, n2)

    jsonresult = {
        'ID': id_val,
        'IDS': ids,
        'K1': k1,
        'K2': k2,
        'K3': k3,
        'K4': k4,
        'N1': n1,
        'N2': n2,
    }

    a_value = obj.calculate_a(obj.ids_val, obj.k1_val, obj.n1_val)

    return HttpResponse(a_value)

