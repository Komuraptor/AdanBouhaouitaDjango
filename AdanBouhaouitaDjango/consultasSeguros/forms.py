from django import forms
from .models import Cita, Medicamento, Medico
import datetime

class CitaForm(forms.ModelForm):

    class Meta:
        model = Cita
        fields = ['idMedico', 'fecha', 'observaciones']
        widgets = {
            'fecha': forms.DateTimeField,
        }

class MedicamentoForm(forms.ModelForm):

    class Meta:
        model = Medicamento
        exclude = ('stock',)

    