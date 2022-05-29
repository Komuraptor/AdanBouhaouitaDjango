from django.contrib import admin
from django.urls import path
from django.conf.urls import include
<<<<<<< Updated upstream
<<<<<<< Updated upstream

urlpatterns = [
    path('admin/', admin.site.urls)
=======
=======
>>>>>>> Stashed changes
from consultasSeguros.views import *

urlpatterns = [

    #Medico
    path('', MedicoList.as_view(template_name = "cruds/medico/medico.html"), name='medico'),
    path('crear', MedicoCrear.as_view(template_name = "cruds/medico/medicoCrear.html"), name = 'medicoCrear'),
    path('editar/<int:pk>', MedicoActualizar.as_view(template_name = "cruds/medico/medicoActualizar.html"), name='medicoActualizar'),
    path('eliminar/<int:pk>', MedicoEliminar.as_view(), name ='medicoEliminar'),

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
]