from django.shortcuts import render
from django.http import HttpResponse
from lmapsim.models import Lmap
from django.template import loader
from django.http import JsonResponse


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

    a_res = obj.calculate_a(obj.ids_val, obj.k1_val, obj.n1_val)
    b_res = obj.calculate_b(obj.k2_val, obj.ids_val, obj.n1_val)
    c_res = obj.calculate_c(obj.ids_val, obj.k3_val, obj.n2_val)
    d_res = obj.calculate_d(obj.id_val, obj.ids_val, obj.n1_val, obj.n2_val)
    ids_up = obj.update_Ids(obj.id_val, obj.ids_val, obj.n2_val, obj.k4_val)
    k1_up = obj.update_k1(obj.k1_val, obj.n2_val, obj.k3_val, obj.id_val)
    k2_up = obj.update_k2(obj.k2_val, obj.n2_val, obj.k4_val, obj.id_val)
    k3_up = obj.update_k3(obj.k3_val, obj.n1_val, obj.k1_val, obj.id_val)
    k4_up = obj.update_k4(obj.k4_val, obj.n1_val, obj.k2_val, obj.id_val)
    n1_ret = obj.retrieve_n1(a_res, obj.k1_val, obj.ids_val)
    n2_ret = obj.retrieve_n2(c_res, obj.ids_val, obj.k3_val)

    json_result = {
        'A': a_res,
        'B': b_res,
        'C': c_res,
        'D': d_res,
        'K1': k1,
        'K2': k2,
        'K3': k3,
        'K4': k4,
        'K1_new': k1_up,
        'K2_new': k2_up,
        'K3_new': k3_up,
        'K4_new': k4_up,
        'N1': n1,
        'N2': n2,
        'IDS_new': ids_up,
        'IDS_old': ids,
        'ID': id_val,
    }

    template_view = loader.get_template('lmapsim/lmapview.html')

    return render(request, 'lmapsim/lmapview.html', json_result)
