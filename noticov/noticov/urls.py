"""noticov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from noticias.views import inicio, listar, articulo, ordenar_tipo, tipos_alcance, ordenar_campo, tipos_campo, control, \
    borrar, nuevoarticulo, nuevoautor, nuevarevista
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('listado', listar, name='lista'),
    path('articulo/<int:id>', articulo),
    path('alcance', ordenar_tipo),
    path('alcance/<int:id>', tipos_alcance),
    path('campo', ordenar_campo),
    path('campo/<int:id>', tipos_campo),
    path('control', control),
    path('borrar/<int:id>', borrar),
    path('nuevoart', nuevoarticulo),
    path('ingreso/', include('django.contrib.auth.urls')),
    path('ingreso/', include('ingreso.urls')),
    path('nuevoautor', nuevoautor),
    path('nuevarevista', nuevarevista),
    path('encuesta/', include('encuesta.urls')),

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
