from django.db import models

# Create your models here.
class Medicamentos(models.Models):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    receta = models.CharField(max_length=1)
    precio = models.FloatField
    stock = models.IntegerField(max_length=11)
