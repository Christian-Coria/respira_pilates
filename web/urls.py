from django.urls import path
from web.views import home
from web.views import About
from web.views import PreguntasFrecuentesVista
from web.views import reglamento
from web.views import PortFolio

urlpatterns = [
    path('',home, name="index"),  
    path('about/', About.as_view(), name="about"),
    path('portfolio/', PortFolio.as_view(), name="portfolio"),
    path("preguntas_frecuentes/", PreguntasFrecuentesVista.as_view(), name="preguntas_frecuentes"),
    path('reglamento/', reglamento, name="reglamento"),


   
]