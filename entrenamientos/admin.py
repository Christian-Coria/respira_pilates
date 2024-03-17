from django.contrib import admin
from .models import Profesor, Membresia, Clase, Asistencia, PeticionInscripcion

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion_meses',)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora_inicio', 'hora_fin', 'profesor', 'membresia',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'clase', 'fecha',)

@admin.register(PeticionInscripcion)
class PeticionInscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'edad', 'peso_aproximado', 'afeccion_fisica', 'tipo_afeccion', 'whatsapp', 'objetivo', 'ha_realizado_actividad_fisica', 'actividad_fisica_realizada', 'disponibilidad_horaria',)
