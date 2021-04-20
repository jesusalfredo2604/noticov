from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    no_persona_var = Persona.objects.count()
    personas = Persona.objects.order_by('-id')
    return render(request, 'bienvenido.html', {'no_personas': no_persona_var, 'personas': personas})
