from django.contrib import admin
from .models import DatosUsuario
from .forms import EditarPerfilForm

class DatosUsuarioAdmin(admin.ModelAdmin):
    form = EditarPerfilForm

admin.site.register(DatosUsuario, DatosUsuarioAdmin)