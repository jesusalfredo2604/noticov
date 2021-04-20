from django.contrib import admin


# Register your models here.
from .models import Autor
from .models import Alcance
from .models import Revista
from .models import Noticia
from .models import Campo
from encuesta.models import Entidad, Genero, Encuestavacunacion, Vacunado

admin.site.register(Revista)
admin.site.register(Autor)
admin.site.register(Campo)
admin.site.register(Alcance)
admin.site.register(Noticia)
admin.site.register(Entidad)
admin.site.register(Genero)
admin.site.register(Encuestavacunacion)
admin.site.register(Vacunado)

