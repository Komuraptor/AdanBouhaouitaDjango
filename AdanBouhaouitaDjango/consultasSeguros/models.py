from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=11)
    fechaalta = models.DateField
    especialidad = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=30, blank = True)
    apellidos = models.CharField(max_length=50, blank = True)
    edad = models.IntegerField(max_length=11)
    direccion = models.CharField(max_length=100, blank = True)
    foto = models.CharField(max_length=100, blank = True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Paciente.objects.create(user = instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Paciente.save()

class Cita(models.Model):
    idPaciente = models.ForeignKey(Paciente, on_delete=CASCADE)
    idMedico = models.ForeignKey(Medico, on_delete=CASCADE)
    fecha = models.DateField
    observaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.fecha

class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    receta = models.CharField(max_length=1)
    precio = models.FloatField
    stock = models.IntegerField(max_length=11)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField
    precio = models.FloatField
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.precio

class Compra_Medicamento(models.Model):
    idMedicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return self.idCompra