from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import DatosUsuario
from django.forms import TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1", "password2"]


class EditarPerfilForm(UserChangeForm):
    new_password = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = DatosUsuario
        fields = (
            'avatar', 'nombre', 'apellido',
            'domicilio','telefono', 'celular', 'documento', 'cuit',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password'].help_text = 'Deja este campo en blanco para no cambiar la contraseña.'

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        if new_password:
            if len(new_password) < 8:
                raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return new_password
