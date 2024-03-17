
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LiberarEspacioForm, NotificarEspacioForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profesor, Membresia, Clase, Asistencia
from .forms import AsistenciaForm

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'lista_profesores.html', {'profesores': profesores})

def lista_membresias(request):
    membresias = Membresia.objects.all()
    return render(request, 'lista_membresias.html', {'membresias': membresias})

def lista_clases(request):
    clases = Clase.objects.all()
    return render(request, 'lista_clases.html', {'clases': clases})

def lista_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'lista_asistencias.html', {'asistencias': asistencias})

def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asistencia registrada correctamente')
            return redirect('lista_asistencias')
    else:
        form = AsistenciaForm()
    return render(request, 'registrar_asistencia.html', {'form': form})


@login_required
def liberar_espacio(request):
    if request.method == 'POST':
        form = LiberarEspacioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Espacio liberado exitosamente.')
            return redirect('dashboard')
    else:
        form = LiberarEspacioForm()
    return render(request, 'liberar_espacio.html', {'form': form})

@login_required
def notificar_espacio(request):
    if request.method == 'POST':
        form = NotificarEspacioForm(request.POST)
        if form.is_valid():
            # Lógica para enviar notificaciones a otros alumnos
            messages.success(request, 'Notificación enviada exitosamente.')
            return redirect('dashboard')
    else:
        form = NotificarEspacioForm()
    return render(request, 'notificar_espacio.html', {'form': form})
