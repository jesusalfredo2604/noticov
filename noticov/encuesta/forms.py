
from django.forms import ModelForm
from django import forms

from .models import Encuestavacunacion


class EncuestaForm(ModelForm):
    class Meta:
        model = Encuestavacunacion
        fields = ('nombre', 'apellido','edad', 'entidad', 'vacunado', 'fecha', 'genero',)

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'entidad': forms.Select(attrs={'class': 'form-control'}),
            'vacunado': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'AÑO-MES-DIA'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),

        }