from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Medico
from .models import Medicamento

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms


#Medico
class MedicoList(ListView):
    model = Medico

class MedicoCrear(SuccessMessageMixin, CreateView):
    model = Medico
    form = Medico
    fields = "__all__"
    success_message = 'Medico Creado'

    def get_success_url(self):
        return reverse('medico')

class MedicoActualizar(SuccessMessageMixin, UpdateView):
    model = Medico
    form = Medico
    fields = "__all__"
    success_message = "Medico actualizado"

    def get_success_url(self):
        return reverse('medico')

class MedicoEliminar(SuccessMessageMixin, DeleteView):
    model = Medico
    form = Medico
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Medico eliminado'
        messages.success(self.request, (success_message))
        return reverse('medico')


#Medicamento
class MedicamentoList(ListView):
    model = Medicamento

class MedicamentoCrear(SuccessMessageMixin, CreateView):
    model = Medicamento
    form = Medicamento
    fields = "__all__"
    success_message = 'Medicamento Creado'

    def get_success_url(self):
        return reverse('medicamento')


class MedicamentoActualizar(SuccessMessageMixin, UpdateView):
    model = Medicamento
    form = Medicamento
    fields = "__all__"
    success_message = "Medicamento actualizado"

    def get_success_url(self):
        return reverse('medicamento')

class MedicamentoEliminar(SuccessMessageMixin, DeleteView):
    model = Medicamento
    form = Medicamento
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Medicamento eliminado'
        messages.success(self.request, (success_message))
        return reverse('medicamento')


# Create your views here.
