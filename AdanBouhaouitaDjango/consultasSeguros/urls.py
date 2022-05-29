from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from consultasSeguros.views import *

urlpatterns = [

    #Medico
    path('', MedicoList.as_view(template_name = "cruds/medico/medico.html"), name='medico'),
    path('crear', MedicoCrear.as_view(template_name = "cruds/medico/medicoCrear.html"), name = 'medicoCrear'),
    path('editar/<int:pk>', MedicoActualizar.as_view(template_name = "cruds/medico/medicoActualizar.html"), name='medicoActualizar'),
    path('eliminar/<int:pk>', MedicoEliminar.as_view(), name ='medicoEliminar'),

]