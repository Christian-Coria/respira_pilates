from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from web.models import PreguntasFrecuentes, Gallery
from django.shortcuts import render
from .models import VisitCounter


def home(request):
    return render(request,'index.html')

class About(TemplateView):
    template_name = "about.html"


class PreguntasFrecuentesVista(View):
    template = "preguntas_frecuentes.html"

    def get(self, request):
        params = {}
        preguntas = PreguntasFrecuentes.objects.all()
        params["preguntas"]=preguntas
        print(params
        )
        return render(request, self.template, params)

def reglamento(request):
    return render(request,'reglamento.html')


def your_page_view(request):
    # Nombre de la página que deseas rastrear
    page_name = "tecnicosenlinea"

    # Buscar el contador de visitas existente o crear uno nuevo
    counter, created = VisitCounter.objects.get_or_create(page_name=page_name)

    # Establecer el contador en 75000 si es un nuevo contador
    if created:
        counter.visit_count = 75000
        counter.save()

    # Incrementar el contador
    counter.visit_count += 1
    counter.save()
    print(counter)

    print("La vista se ha llamado correctamente")
    return render(request, 'snippets/visitantes.html', {'counter': counter})


def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)

class PortFolio(TemplateView):
    template_name = "portfolio.html"