from django.db import models
from operations import bitfunctions


# Create your models here.

class Sasi(models.Model):
    max = 16
    id_val = models.BinaryField(max)
    ids_val = models.BinaryField(max_length=16)
    k1_val = models.BinaryField(max_length=16)
    k2_val = models.BinaryField(max_length=16)
    n1_val = models.BinaryField(max_length=16)
    n2_val = models.BinaryField(max_length=16)
    A_val = models.BinaryField(max_length=16)
    B_val = models.BinaryField(max_length=16)
    C_val = models.BinaryField(max_length=16)
    D_val = models.BinaryField(max_length=16)

    def __init__(self, id_, ids, k1, k2, n1, n2):
        self.id_val = id_
        self.ids_val = ids
        self.k1_val = k1
        self.k2_val = k2
        self.n1_val = n1
        self.n2_val = n2

    def calculate_a(self, ids, k1, n1):
        value = (int(ids, 2) ^ int(k1, 2)) ^ int(n1, 2)
        res = format(value, '008b')
        return res

    def calculate_b(self, k2, ids, n2):
        value = (int(ids, 2) | int(k2, 2)) & int(n2, 2)
        res = format(value, '008b')
        return res

    def calculate_c(self, k1, k2_up, k1_up, k2):
        value = (int(k2_up, 2) ^ int(k1, 2)) & (int(k1_up, 2) ^ int(k2, 2))
        res = format(value, '008b')
        return res

    def calculate_d(self, id_, k2_up, k2, k1, k1_up):
        value = (int(k2_up, 2) & int(id_, 2)) ^ ((int(k1, 2) ^ int(k2, 2)) | int(k1_up, 2))
        res = format(value, '008b')
        return res

    def update_Ids(self, id_, ids, n2, k1_up):
        value = (int(ids, 2) & int(id_, 2)) ^ (int(n2, 2) ^ int(k1_up, 2))
        res = format(value, '008b')
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
    def update_k1(self, k2, n1, k1, r):
        seedval = bitfunctions.seed(bitfunctions.hemmingweight(r))
        rhk2 = bitfunctions.recursivehash(k2, r)
        rhn1 = bitfunctions.recursivehash(n1, r)
        rotrhk2n1 = bitfunctions.rotleft2(rhk2, bitfunctions.hemmingweight(rhn1))
        return bitfunctions.andbin(rotrhk2n1, k1)

    def update_k(self, k2, n1):
        res = int(k2, 2) ^ int(n1, 2)
        value = format(res, '008b')
        hw = bitfunctions.hemmingweight(k2)
        rotl = bitfunctions.rotleft2(value, hw)
        return rotl

