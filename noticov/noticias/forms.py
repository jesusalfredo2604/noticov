# from django.forms import ModelForm

from django.contrib.auth import forms
from django.forms import ModelForm

from django import forms
from .models import Noticia, Revista, Autor


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'fecha', 'campo', 'alcance', 'autor', 'revista', 'resumen', 'weblink')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre del articulo'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'AÑO-MES-DIA'}),
            'campo': forms.Select(attrs={'class': 'form-control'}),
            'alcance': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'revista': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'breve descripcion del articulo'}),
            'weblink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enlace para acceder al articulo'}),
        }


class RevistaForm(ModelForm):
    class Meta:
        model = Revista
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }
