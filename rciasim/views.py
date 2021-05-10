from django.http import HttpResponse
from django.shortcuts import render, redirect
from validations import isValid
from django.contrib import messages
from validations import isValid

import rciasim.views
from operations import bitfunctions
from .models import PostForm

# Create your views here.
from rciasim.models import Rcia


def rciasubmit(request):
    if request.POST:
        id_val = request.POST.get("rciaId")
        ids = request.POST.get("rciaIds")
        k1 = request.POST.get("rciaK1")
        k2 = request.POST.get("rciaK2")
        n1 = request.POST.get("rciaN1")
        n2 = request.POST.get("rciaN2")

        if not isValid.is_valid_rcia(id_val, ids, k1, k2, n1, n2):
            messages.error(request, 'Error! Please enter 16 bit binary values in all fields!')
            return redirect(rciasim.views.rcia)
        else:

            obj = Rcia(id_val, ids, k1, k2, n1, n2)

            seed = obj.seed(bitfunctions.xorbin(n1, n2))
            a = obj.calculate_a(ids, k1, n1)
            b = obj.calculate_b(ids, n1, k2, k1)
            k1_up = obj.update_k(k2, n1, k1, seed)
            k2_up = obj.update_k(k1, n2, k2, seed)
            c = obj.calculate_c(k1_up, k2_up, n1, n2, seed)
            d = obj.calculate_d(id_val, k1_up, k2_up, n2, ids, seed)
            ids_up = obj.update_Ids(ids, n2, n1, seed)
            rhk1up = bitfunctions.recursivehash(k1_up, seed)
            rhk2up = bitfunctions.recursivehash(k2_up, seed)
            rhn1 = bitfunctions.recursivehash(n1, seed)
            rhn2 = bitfunctions.recursivehash(n2, seed)
            rotrhnarhn2 = bitfunctions.rotleft2(rhn1, bitfunctions.hemmingweight(rhn2))
            # rot of ids and k1
            rotidsk1 = bitfunctions.rotleft2(ids, bitfunctions.hemmingweight(k1))
            # and of ids and n1
            idsandn1 = bitfunctions.andbin(ids, n1)
            k1xorn2 = bitfunctions.xorbin(k1, n2)
            k2xorn1 = bitfunctions.xorbin(k2, n1)
            # rotation of the result of ids and n1 by the hemming weight of n1
            rotidsn1k2 = bitfunctions.rotleft2(idsandn1, bitfunctions.hemmingweight(n1))
            # this is too long but this is the D calculation in RCIA good luck future me
            rotidsn1k2andk1 = bitfunctions.andbin(bitfunctions.rotleft2(bitfunctions.andbin(ids, n1), bitfunctions.hemmingweight(k2)), k1)
            # if you're looking at this and you dont know what's going on, I am sorry it's my fault this is D calc
            rotrhidshwk1up = bitfunctions.rotleft2(bitfunctions.recursivehash(id_val, seed), bitfunctions.hemmingweight(k1_up))
            # D calculation once again
            rotrhk2uphwrhn2 = bitfunctions.rotleft2(bitfunctions.recursivehash(k2_up, seed), bitfunctions.hemmingweight(bitfunctions.recursivehash(n2, seed)))
            # 2nd to the final calculation to attain D value
            dandval = bitfunctions.andbin(rotrhidshwk1up, rotrhk2uphwrhn2)

            print("type of A: ", type(a))
            json_result = {
                'seed': seed,
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
                'rotidsk1': rotidsk1,
                'idsandn1': idsandn1,
                'rotidsn1k2': rotidsn1k2,
                'hwk1': bitfunctions.hemmingweight(k1),
                'hwk2': bitfunctions.hemmingweight(k2),
                'R': bitfunctions.xorbin(n1, n2),
                'rhk1up': rhk1up,
                'rhk2up':rhk2up,
                'hwr': bitfunctions.hemmingweight(bitfunctions.xorbin(n1, n2)),
                'rhn1': rhn1,
                'rhn2': rhn2,
                'rotidsn1k2andk1': rotidsn1k2andk1,
                'rotrhk2uphwrhn2': rotrhk2uphwrhn2,
                'dandval': dandval,
                'rotrhnarhn2': rotrhnarhn2,
                'k1xorn2': k1xorn2,
                'k2xorn1': k2xorn1,
            }
            return render(request, 'rciasim/rciaview.html', json_result)
    else:
        return render(request, 'rciasim/rciaview.html')


def home(request):
    return render(request, 'homepage.html')


def lmap(request):
    return render(request, 'lmapsim/lmapview.html')


def sasi(request):
    return render(request, 'sasisim/sasiview.html')


def rcia(request):
    return render(request, 'rciasim/rciaview.html')
