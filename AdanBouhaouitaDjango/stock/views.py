from ast import Del
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Medicamento

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

# Create your views here.
class MedicamentoList(ListView):
    model = Medicamento

class MedicamentoActualizar(SuccessMessageMixin, UpdateView):
    model = Medicamento
    form = Medicamento
    fields = "__all__"
    success_message = "Medicamento actualizado"

    def get_success_url(self):
        return reverse('medicamento')