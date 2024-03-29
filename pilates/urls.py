from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')), # es el path para redux user
    path('captcha/', include('captcha.urls')),
    path('contacto/', include('contacto.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('entrenamientos/', include('entrenamientos.urls')),
    path('', include('web.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),    
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += path('__debug__/', include('debug_toolbar.urls')),