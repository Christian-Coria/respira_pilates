from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from simple_history.models import HistoricalRecords


class PreguntasFrecuentes(models.Model):

    pregunta = models.CharField(max_length=160, blank=True, null=True)
    descripcion = models.TextField( blank=True, null=True)
    contenido = RichTextUploadingField('contenido', blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = "Preguntas Frecuentes"
        verbose_name_plural = "Preguntas Frecuentes"



class VisitCounter(models.Model):
    page_name = models.CharField(max_length=255, unique=True)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.page_name