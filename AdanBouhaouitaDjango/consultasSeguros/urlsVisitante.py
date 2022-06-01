from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from consultasSeguros.views import *
from django.views.generic.base import TemplateView

urlpatterns = [

    #Visitante
    path('', TemplateView.as_view(template_name='homeVisitante.html'), name='homeVisitante'),
    path('medicoVisitante/', MedicoVisitanteList.as_view(template_name = "cruds/visitante/medicoVisitante.html"), name = 'medicoVisitante'),

]