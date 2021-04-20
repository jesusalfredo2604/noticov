from django.db import models


# Create your models here.
class Revista(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Campo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alcance(models.Model):
    alcance = models.CharField(max_length=50)

    def __str__(self):
        return self.alcance


class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    fecha = models.DateTimeField()
    campo = models.ForeignKey(Campo, on_delete=models.SET_NULL, null=True)
    alcance = models.ForeignKey(Alcance, on_delete=models.SET_NULL, null=True)
    autor = models.ManyToManyField(Autor, blank=True)
    revista = models.ManyToManyField(Revista, blank=True)
    resumen = models.TextField(blank=True)
    weblink = models.URLField(null=True)

    def __str__(self):
        return self.titulo
