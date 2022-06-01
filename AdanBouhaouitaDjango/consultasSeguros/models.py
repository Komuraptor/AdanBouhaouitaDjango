from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import datetime
from django.core.exceptions import ValidationError

# Create your models here.
class Medico(models.Model):
    med_familia = 'Médico de familia'
    digestivo = 'Digestivo'
    neurologo = 'Neurologo'
    dermatologo = 'Dermatólogo'
    traumatologo = 'Traumatólogo'
    ESPECIALIDADES = (
        (med_familia, 'Médico de familia'),
        (digestivo, 'Digestivo'),
        (neurologo, 'Neurologo'),
        (dermatologo, 'Dermatólogo'),
        (traumatologo, 'Traumatólogo')
    )

    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    edad = models.CharField(max_length=2)
    fechaalta = models.DateTimeField(auto_now_add = True)
    especialidad = models.CharField(max_length=25, choices = ESPECIALIDADES, default=med_familia)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    apellidos = models.CharField(max_length=50, null = True)
    edad = models.CharField(max_length=2, null = True)
    direccion = models.CharField(max_length=100, null = True)
    foto = models.ImageField(upload_to='imagenes/', null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Paciente.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.paciente.save()

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.is_active = False

class Cita(models.Model):
    idPaciente = models.ForeignKey(User, on_delete=CASCADE)
    idMedico = models.ForeignKey(Medico, on_delete=CASCADE)
    fecha = models.DateField()
    observaciones = models.CharField(max_length=200)

    def __str__(self):
        return str(self.fecha)
    
    def clean(self):
        if(self.fecha < datetime.date.today()):
            raise ValidationError("Elija una fecha a partir de hoy")

class Medicamento(models.Model):
    s = 's'
    n = 'n'
    TIPO_RECETA = (
        (s, 'Con receta'),
        (n, 'Venta libre')
    )

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    receta = models.CharField(max_length=1, choices=TIPO_RECETA)
    precio = models.CharField(max_length=10)
    stock = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField()
    precio = models.CharField(max_length=10)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.precio

class Compra_Medicamento(models.Model):
    idMedicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return self.idCompra