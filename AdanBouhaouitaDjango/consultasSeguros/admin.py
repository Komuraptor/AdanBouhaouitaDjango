from django.contrib import admin
from consultasSeguros.forms import CitaForm

from consultasSeguros.models import Cita, Compra, Compra_Medicamento, Medicamento, Medico, Paciente

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad', 'fechaalta', 'especialidad', 'username', 'password')

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad', 'direccion')

class CitaAdmin(admin.ModelAdmin):
    form = CitaForm
    list_display = ('idPaciente', 'idMedico', 'fecha', 'observaciones')

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'receta', 'precio', 'stock')

class CompraAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'precio', 'idPaciente')

class CompraMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('idMedicamento', 'idCompra')

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cita, CitaAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Compra_Medicamento, CompraMedicamentoAdmin)
