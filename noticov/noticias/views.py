# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NoticiaForm, AutorForm, RevistaForm
from .models import Noticia, Alcance, Campo


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def listar(request):
    lista_noticias = Noticia.objects.order_by('-fecha')

    return render(request, 'listado.html', {
        'lista_noticias': lista_noticias
    })


def articulo(request, id):
    articulo = Noticia.objects.get(pk=id)
    # persona = get_object_or_404(persona, pk=id)
    return render(request, 'articulo.html', {'articulo': articulo})


def ordenar_tipo(request):
    lista_tipos = Alcance.objects.all()
    return render(request, 'alcance.html', {'alcances': lista_tipos})


def tipos_alcance(request, id):
    ntipos = Alcance.objects.get(pk=id)
    todas = Noticia.objects.order_by('-fecha')
    return render(request, 'tipo.html', {'ntipos': ntipos,
                                         'todas': todas})


def ordenar_campo(request):
    lista_campos = Campo.objects.all()
    return render(request, 'campo.html', {'campos': lista_campos})

def tipos_campo(request, id):
    ntipos = Campo.objects.get(pk=id)
    todas = Noticia.objects.order_by('-fecha')
    return render(request, 'tipo_campo.html', {'ntipos': ntipos,
                                         'todas': todas})

def control(request):
    todas = Noticia.objects.order_by('id')
    return render(request, 'control.html', {'todas': todas})

def borrar (request,id):

    objeto = get_object_or_404(Noticia, pk=id)

    if objeto:
        objeto.delete()
    todas = Noticia.objects.order_by('id')
    return render(request, 'control.html', {'todas': todas})


def nuevoarticulo(request):
    if request.method == 'POST':
        formaarticulo = NoticiaForm(request.POST)
        if formaarticulo.is_valid():
            formaarticulo.save()
            todas = Noticia.objects.order_by('id')
            return render(request, 'control.html', {'todas': todas})


    else:
        formaarticulo = NoticiaForm()

    return render(request, 'nuevoarticulo.html', {'formaarticulo': formaarticulo})


def nuevoautor(request):
    if request.method == 'POST':
        formaautor = AutorForm(request.POST)
        if formaautor.is_valid():
            formaautor.save()
            todas = Noticia.objects.order_by('id')
            return render(request, 'control.html', {'todas': todas})


    else:
        formaautor = AutorForm()

    return render(request, 'nuevoautor.html', {'formaautor': formaautor})


def nuevarevista(request):
    if request.method == 'POST':
        formarevista = RevistaForm(request.POST)
        if formarevista.is_valid():
            formarevista.save()
            todas = Noticia.objects.order_by('id')
            return render(request, 'control.html', {'todas': todas})


    else:
        formarevista = RevistaForm()

    return render(request, 'nuevarevista.html', {'formarevista': formarevista})
