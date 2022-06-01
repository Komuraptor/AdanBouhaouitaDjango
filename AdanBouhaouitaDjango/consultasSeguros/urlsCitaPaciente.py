from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from consultasSeguros.views import *

urlpatterns = [

    #CitaPaciente
    path('', CitaList.as_view(template_name = "cruds/cita/citaPaciente.html"), name='citaPaciente'),
    path('crear', CitaCrear.as_view(template_name = "cruds/cita/citaCrear.html"), name = 'citaCrear'),
    path('eliminar/<int:pk>', CitaEliminar.as_view(), name ='citaEliminar'),

]