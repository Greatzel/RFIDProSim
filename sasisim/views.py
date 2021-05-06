from django.shortcuts import render, redirect

import sasisim.views
from sasisim.models import Sasi
from operations import bitfunctions
from django.contrib import messages
from validations import isValid
from django.http import HttpResponse


# Create your views here.

def sasisubmit(request):
    if request.POST:
        id_val = request.POST.get("sasiId")
        ids = request.POST.get("sasiIds")
        k1 = request.POST.get("sasiK1")
        k2 = request.POST.get("sasiK2")
        n1 = request.POST.get("sasiN1")
        n2 = request.POST.get("sasiN2")

        if not isValid.is_valid_sasi(id_val, ids, k1, k2, n1, n2):
            messages.error(request, 'Error! Please enter 8 to 16 bits!')
            return redirect(sasisim.views.sasisubmit)
        else:
            obj = Sasi(id_val, ids, k1, k2, n1, n2)
            a = obj.calculate_a(ids, k1, n1)
            b = obj.calculate_b(k2, ids, n2)
            k1_up = obj.update_k(k1, n2)
            k2_up = obj.update_k(k2, n1)
            c = obj.calculate_c(k1, k2_up, k1_up, k2)
            d = obj.calculate_d(id_val, k2_up, k2, k1, k1_up)
            ids_up = obj.update_Ids(id_val, ids, n2, k1_up)
            ids_xor_k1 = bitfunctions.xorbin(ids, k1)
            ids_or_k2 = bitfunctions.orbin(ids, k2)

            json_result = {
                'A': a,
                'B': b,
                'C': c,
                'D': d,
                'K1': k1,
                'K2': k2,
                'K1_new': k1_up,
                'K2_new': k2_up,
                'N1': n1,
                'N2': n2,
                'IDS_new': ids_up,
                'IDS_old': ids,
                'ID': id_val,
                'ids_xor_k1': ids_xor_k1,
                'ids_or_k2': ids_or_k2,
                'k1_xor_n2': bitfunctions.xorbin(k1, n2),
                'k2_xor_n1': bitfunctions.xorbin(k2, n1),
                'k1_xor_k2up': bitfunctions.xorbin(k1, k2_up),
                'k1_xor_k2': bitfunctions.xorbin(k1, k2),
                'k2up_and_id': bitfunctions.andbin(k2_up, id_val),
                'ids_and_id': bitfunctions.andbin(ids, id_val),
                'n2_xor_k1': bitfunctions.xorbin(n2, k1_up)
            }
            return render(request, 'sasisim/sasiview.html', json_result)
    else:
        return render(request, 'sasisim/sasiview.html')


def home(request):
    return render(request, 'homepage.html')


def lmap(request):
    return render(request, 'lmapsim/lmapview.html')


def rcia(request):
    return render(request, 'rciasim/rciaview.html')


def sasi(request):
    return render(request, 'sasisim/sasiview.html')
