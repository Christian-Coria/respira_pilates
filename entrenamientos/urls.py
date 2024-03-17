from django.urls import path
from . import views

urlpatterns = [
    path('liberar-espacio/', views.liberar_espacio, name='liberar_espacio'),
    path('notificar-espacio/', views.notificar_espacio, name='notificar_espacio'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('membresias/', views.lista_membresias, name='lista_membresias'),
    path('clases/', views.lista_clases, name='lista_clases'),
    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
]

