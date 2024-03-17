from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['usuario', 'clase', 'fecha']

    def __init__(self, *args, **kwargs):
        super(AsistenciaForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['clase'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha'].widget.attrs.update({'class': 'form-control', 'type': 'date'})

class LiberarEspacioForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = []

class NotificarEspacioForm(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea)
