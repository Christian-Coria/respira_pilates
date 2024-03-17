from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)

class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    duracion_meses = models.IntegerField()

class Clase(models.Model):
    dia = models.CharField(max_length=20)  
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)

class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha = models.DateField()


class PeticionInscripcion(models.Model):
    OPCIONES_AFECCION_FISICA = [
        ('SI', 'Sí'),
        ('NO', 'No')
    ]

    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso_aproximado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    afeccion_fisica = models.CharField(max_length=2, choices=OPCIONES_AFECCION_FISICA)
    tipo_afeccion = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=20)
    objetivo = models.TextField()
    ha_realizado_actividad_fisica = models.CharField(max_length=2, choices=OPCIONES_AFECCION_FISICA)
    actividad_fisica_realizada = models.CharField(max_length=100, blank=True, null=True)
    disponibilidad_horaria = models.TextField()
    

    def __str__(self):
        return self.nombre_completo
