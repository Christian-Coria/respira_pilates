from django.urls import path
from usuarios import views
from usuarios.views_login import pagina_login
from usuarios.views_logout import pagina_logout
from usuarios.views_registro import pagina_registro
from usuarios.views_perfil import perfil
from usuarios.views_perfil import EditarPerfil
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', pagina_login, name="login"),
    path('logout', pagina_logout, name="logout"),
    path('registro', pagina_registro, name="registro"),
    path("perfil", perfil, name="perfil"),
    path("editar-perfil/<int:pk>/", EditarPerfil.as_view(), name="editar_perfil"),

    
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
