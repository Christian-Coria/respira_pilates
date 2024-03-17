from django.contrib import admin
from .models import PreguntasFrecuentes, VisitCounter, Gallery

@admin.register(PreguntasFrecuentes)
class PreguntasFrecuentesAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'descripcion', 'contenido',)
    search_fields = ('pregunta', 'descripcion',)
    list_filter = ('pregunta',)

@admin.register(VisitCounter)
class VisitCounterAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'visit_count',)
    search_fields = ('page_name',)
    list_filter = ('page_name',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'timeStamp',)
    search_fields = ('title',)
    list_filter = ('timeStamp',)

