from django.db import models

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


def calculateA(self):
    return self