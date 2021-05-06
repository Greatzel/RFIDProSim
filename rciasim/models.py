from django.db import models
from operations import bitfunctions
from django.forms import ModelForm
from django import forms


# Create your models here.

class Rcia(models.Model):
    id_val = models.BinaryField(max_length=16, editable=True)
    ids_val = models.BinaryField(max_length=16, editable=True)
    k1_val = models.BinaryField(max_length=16, editable=True)
    k2_val = models.BinaryField(max_length=16, editable=True)
    n1_val = models.BinaryField(max_length=16, editable=True)
    n2_val = models.BinaryField(max_length=16, editable=True)
    A_val = models.BinaryField(max_length=16, editable=True)
    B_val = models.BinaryField(max_length=16, editable=True)
    C_val = models.BinaryField(max_length=16, editable=True)
    D_val = models.BinaryField(max_length=16, editable=True)

    def __init__(self, id_, ids, k1, k2, n1, n2):
        self.id_val = id_
        self.ids_val = ids
        self.k1_val = k1
        self.k2_val = k2
        self.n1_val = n1
        self.n2_val = n2

    def calculate_a(self, ids, k1, n1):
        rotval = bitfunctions.rotleft(ids, bitfunctions.hemmingweight(k1))
        value = int(rotval, 2) ^ int(n1, 2)
        res = format(value, '008b')
        return res

    def calculate_b(self, ids, n1, k2, k1):
        first = bitfunctions.andbin(ids, n1)
        rotval = bitfunctions.rotleft(first, bitfunctions.hemmingweight(k2))
        value = int(bitfunctions.andbin(rotval, k1), 2) ^ int(n1, 2)
        res = format(value, '008b')
        return res

    # rcia cal c
    def calculate_c(self, k1_up, k2_up, n1, n2, s):
        # print(type(s))
        # print(type(n1))
        rhk1up = bitfunctions.recursivehash(k1_up, s)
        rhk2up = bitfunctions.recursivehash(k2_up, s)
        # print("rhk2up: ", rhk2up)
        rhn1 = bitfunctions.recursivehash(n1, s)
        # print("rhn1: ", rhn1)
        rhn2 = bitfunctions.recursivehash(n2, s)
        # print("rhn2: ", rhn2)
        rotk1k2 = bitfunctions.rotleft2(rhk1up, bitfunctions.hemmingweight(rhk2up))
        # print("rot rhk1, hw(rhk2)", rotk1k2)
        rotn1n2 = bitfunctions.rotleft2(rhn1, bitfunctions.hemmingweight(rhn2))
        # print("rot rhn1, hw(rhn2)", rotn1n2)
        value = bitfunctions.andbin(rotk1k2, rotn1n2)
        # this returns a string
        return value

    def calculate_d(self, id_, k1_up, k2_up, n2, ids, s):
        first = bitfunctions.rotleft2(bitfunctions.recursivehash(id_, s), bitfunctions.hemmingweight(k1_up))
        second = bitfunctions.rotleft2(bitfunctions.recursivehash(k2_up, s), bitfunctions.hemmingweight(
            bitfunctions.recursivehash(n2, s)))
        third = bitfunctions.andbin(first, second)
        fourth = bitfunctions.xorbin(third, ids)
        return fourth

    def update_Ids(self, ids, n2, n1, s):
        rhids = bitfunctions.recursivehash(ids, s)
        rhidsxn2 = bitfunctions.xorbin(rhids, n2)
        res = bitfunctions.rotleft2(rhidsxn2, bitfunctions.hemmingweight(n1))
        return res

    def retrieve_n1(self, a, k1, ids):
        value = (int(a, 2) ^ int(k1, 2)) ^ int(ids, 2)
        res = format(value, '008b')
        return res

    def retrieve_n2(self, b, ids, k2):
        value = (int(ids, 2) | int(k2, 2)) ^ int(b, 2)
        res = format(value, '008b')
        return res

    # rcia k1 update
    def update_k(self, k2, n1, k1, seed):
        rhk2 = bitfunctions.recursivehash(k2, seed)
        rhn1 = bitfunctions.recursivehash(n1, seed)
        rotrhk2n1 = bitfunctions.rotleft2(rhk2, bitfunctions.hemmingweight(rhn1))
        return bitfunctions.andbin(rotrhk2n1, k1)

    # bin1 is the hw of R
    # K is 4 always! refer to paper
    def seed(self, bin1):
        res = bitfunctions.hemmingweight(int(bin1, 2)) % 4
        return res


class PostForm(ModelForm):
    class Meta:
        model = Rcia

        fields = ["id_val", "ids_val", "k1_val", "k2_val", "n1_val", "n2_val"]

    def clean(self):
        super(PostForm, self).clean()

        idval = self.cleaned_data.get('id_val')
        ids = self.cleaned_data.get('ids_val')
        k1 = self.cleaned_data.get('k1_val')
        k2 = self.cleaned_data.get('k2_val')
        n1 = self.cleaned_data.get('n1_val')
        n2 = self.cleaned_data.get('rciaN2')

        if len(idval) or len(ids) or len(k1) or len(k2) or len(n1) or len(n2) < 16:
            self._errors['idval'] = self.error_class(['Enter 16 bit value'])
            self._errors['ids'] = self.error_class(['Enter 16 bit value'])
            self._errors['k1'] = self.error_class(['Enter 16 bit value'])
            self._errors['k2'] = self.error_class(['Enter 16 bit value'])
            self._errors['n1'] = self.error_class(['Enter 16 bit value'])
            self._errors['n2'] = self.error_class(['Enter 16 bit value'])

        return self.cleaned_data
