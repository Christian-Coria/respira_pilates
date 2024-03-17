from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time


class DatosUsuario(models.Model):
    usuario              = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", default='defecto/defecto.png', blank=True, null=True) 
    nombre               = models.CharField(max_length=50)
    apellido             = models.CharField(max_length=50)
    domicilio            = models.CharField(max_length=80, blank=True)
    telefono             = models.CharField(max_length=30, blank=True)
    celular              = models.CharField(max_length=30, blank=True)
    documento            = models.CharField(max_length=30, blank=True)
    cuit                 = models.CharField(max_length=30, blank=True)



    def __str__(self):
        return self.usuario.username

