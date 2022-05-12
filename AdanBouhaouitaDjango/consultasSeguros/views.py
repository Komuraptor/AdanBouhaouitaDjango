from ast import Del
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Medico

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

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





