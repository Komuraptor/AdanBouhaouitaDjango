import django_filters
from .models import Cita, Medico

class MedicoFilter(django_filters.FilterSet):
    class Meta:
        model = Medico
        fields = ['especialidad']

class CitaMedicoFilter(django_filters.FilterSet):
    class Meta:
        model = Cita
        fields = ['fecha']