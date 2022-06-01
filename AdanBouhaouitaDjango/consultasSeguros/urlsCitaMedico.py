from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from consultasSeguros.views import *

urlpatterns = [

    #CitaPaciente
    path('', CitaList.as_view(template_name = "cruds/cita/citaMedico.html"), name='citaMedico'),
    path('editar/<int:pk>', CitaActualizar.as_view(template_name = "cruds/cita/citaActualizar.html"), name='citaActualizar'),

]