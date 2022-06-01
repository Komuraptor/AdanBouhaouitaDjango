from ast import Del
from datetime import datetime
from time import timezone
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cita, Medico, Medicamento

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

from .filters import CitaMedicoFilter, MedicoFilter

from .forms import CitaForm, MedicamentoForm

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
    success_message = 'Medicamento creado'

    def get_success_url(self):
        return reverse('medicamento')


class MedicamentoActualizar(SuccessMessageMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    success_message = "Medicamento actualizado"

    def get_success_url(self):
        return reverse('medicamento')

class MedicamentoAumentarStock(SuccessMessageMixin, UpdateView):
    model = Medicamento
    form = Medicamento
    fields = ['stock']
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


#Cita
class CitaList(ListView):
    model = Cita

class CitaMedicoList(ListView):
    model = Cita
    filter_class = CitaMedicoFilter

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['filter'] = datetime.today().strftime('%e de %B de %Y')
        # context['filter'] = Cita.objects.filter(date__range=(today_min, today_max))        
        # context = super().get_context_data(**kwargs)
        # context['filter'] = CitaMedicoFilter(self.request.GET, queryset=self.get_queryset())
        # return context

        context = super().get_context_data(**kwargs)
        medico = Medico.objects.get(nombre=self.request.user)
        hoy = datetime.today().strftime('%e de %B de %Y')
        citasHoy = Cita.objects.filter(idMedico=medico).filter(fecha=str(hoy))
        
        context['filter'] = MedicoFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CitaCrear(SuccessMessageMixin, CreateView):
    model = Cita
    form = CitaForm
    fields = ['idMedico', 'fecha', 'observaciones']
    success_message = 'Cita Creada'

    def get_success_url(self):
        return reverse('citaPaciente')
    
    def form_valid(self, form):
        form.instance.idPaciente=self.request.user
        return super().form_valid(form)

class CitaActualizar(SuccessMessageMixin, UpdateView):
    model = Cita
    form = Cita
    fields = "__all__"
    success_message = "Cita actualizada"

    def get_success_url(self):
        return reverse('citaMedico')

class CitaEliminar(SuccessMessageMixin, DeleteView):
    model = Cita
    form = Cita
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Cita eliminada'
        messages.success(self.request, (success_message))
        return reverse('citaPaciente')


#Visitante
class MedicoVisitanteList(ListView):
    model = Medico
    filter_class = MedicoFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MedicoFilter(self.request.GET, queryset=self.get_queryset())
        return context

