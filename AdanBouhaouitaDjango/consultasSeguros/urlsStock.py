from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from consultasSeguros.views import *

urlpatterns = [

    #Medicamento
    path('', MedicamentoList.as_view(template_name = "cruds/medicamento/medicamento.html"), name = 'medicamento'),
    path('crear', MedicamentoCrear.as_view(template_name = "cruds/medicamento/medicamentoCrear.html"), name = 'medicamentoCrear'),
    path('editar/<int:pk>', MedicamentoActualizar.as_view(template_name = "cruds/medicamento/medicamentoActualizar.html"), name='medicamentoActualizar'),
    path('eliminar/<int:pk>', MedicamentoEliminar.as_view(), name ='medicamentoEliminar'),

]