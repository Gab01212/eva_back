from django.contrib import admin
from .models import EspecialidadMedica, PrestacionMedica

# 1. Personalización de Títulos Globales del Admin
admin.site.site_header = 'RedSalud Vital - Panel de Control'
admin.site.site_title = 'RedSalud Vital Admin'
admin.site.index_title = 'Gestión Operativa de Recursos y Servicios'

@admin.register(EspecialidadMedica)
class EspecialidadMedicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activa')
    search_fields = ('nombre',)
    list_editable = ('activa',)

@admin.register(PrestacionMedica)
class PrestacionMedicaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'especialidad', 'arancel_base', 'estado', 'vigente')
    list_filter = ('especialidad', 'estado', 'vigente')
    search_fields = ('codigo', 'titulo', 'descripcion')
    list_editable = ('arancel_base', 'estado', 'vigente')
    fieldsets = (
        ('Identificación del Recurso', {
            'fields': ('codigo', 'titulo', 'especialidad')
        }),
        ('Detalle Económico y Operativo', {
            'fields': ('arancel_base', 'duracion_minutos', 'estado', 'vigente')
        }),
        ('Multimedia y Contenido', {
            'fields': ('descripcion', 'imagen')
        }),
    )