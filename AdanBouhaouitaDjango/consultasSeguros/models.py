from tkinter import CASCADE
from django.db import models

# Create your models here.
class Medicos(models.Models):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=11)
    fechaalta = models.DateField
    especialidad = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Pacientes(models.Models):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=11)
    direccion = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Citas(models.Models):
    idPaciente = models.ForeignKey(Pacientes, on_delete=CASCADE)
    idMedico = models.ForeignKey(Medicos, on_delete=CASCADE)
    fecha = models.DateField
    observaciones = models.CharField(max_length=200)

class Medicamentos(models.Models):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    receta = models.CharField(max_length=1)
    precio = models.FloatField
    stock = models.IntegerField(max_length=11)

class Compra(models.Models):
    fecha = models.DateField
    precio = models.FloatField
    idPaciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)

class Compra_Medicamentos(models.Models):
    idMedicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)