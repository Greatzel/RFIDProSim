from django.db import models
from operations import additionaloperations


# Create your models here.

class Lmap(models.Model):
    id_val = models.BinaryField(max_length=16)
    ids_val = models.BinaryField(max_length=16)
    k1_val = models.BinaryField(max_length=16)
    k2_val = models.BinaryField(max_length=16)
    k3_val = models.BinaryField(max_length=16)
    k4_val = models.BinaryField(max_length=16)
    n1_val = models.BinaryField(max_length=16)
    n2_val = models.BinaryField(max_length=16)
    A_val = models.BinaryField(max_length=16)
    B_val = models.BinaryField(max_length=16)
    C_val = models.BinaryField(max_length=16)
    D_val = models.BinaryField(max_length=16)

    def __init__(self, id_, ids, k1, k2, k3, k4, n1, n2):
        self.id_val = id_
        self.ids_val = ids
        self.k1_val = k1
        self.k2_val = k2
        self.k3_val = k3
        self.k4_val = k4
        self.n1_val = n1
        self.n2_val = n2

    def calculate_a(self, ids, k1, n1):
        value = (int(ids, 2) ^ int(k1, 2)) ^ int(n1, 2)
        res = format(value, '008b')
        return res

    def calculate_b(self, k2, ids, n1):
        value = (int(ids, 2) | int(k2, 2)) & int(n1, 2)
        res = format(value, '008b')
        return res

    def calculate_c(self, ids, k3, n2):
        value = (int(ids, 2) & int(k3, 2)) & int(n2, 2)
        res = format(value, '008b')
        return res

    def calculate_d(self, id_, ids, n1, n2):
        value = ((int(ids, 2) & int(id_, 2)) ^ int(n1, 2)) ^ n2
        res = format(value, '008b')
        return res

    # write key updating methods

    def update_Ids(self, id_, ids, n2, k4):
        value = (int(ids, 2) & (int(n2, 2) ^ int(k4, 2))) ^ id_
        res = format(value, '008b')
        return res

    def update_k1(self, k1, n2, k3, id_):
        value = (int(k1, 2) ^ int(n2, 2)) ^ (int(k3, 2) & int(id_, 2))
        res = format(value, '008b')
        return res

    def update_k2(self, k2, n2, k4, id_):
        value = (int(k2, 2) ^ int(n2, 2)) ^ (int(k4, 2) & int(id_, 2))
        res = format(value, '008b')
        return res

    def update_k3(self, k3, n1, k1, id_):
        value = (int(k3, 2) ^ int(n1, 2)) & (int(k1, 2) ^ int(id_, 2))
        res = format(value, '008b')
        return res

    def update_k4(self, k4, n1, k2, id_):
        value = (int(k4, 2) ^ int(n1, 2)) & (int(k2, 2) ^ int(id_, 2))
        res = format(value, '008b')
        return res
