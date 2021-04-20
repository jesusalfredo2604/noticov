from django.db import models


# Create your models here.
class Entidad(models.Model):
    estado = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.estado}'


class Genero(models.Model):
    sexo = models.CharField(max_length=50)

    def __str__(self):
        return f' genero: {self.sexo}'


class Vacunado(models.Model):
    vacuna = models.CharField(max_length=150)

    def __str__(self):
        return f' Estado: {self.vacuna}'


class Encuestavacunacion(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    edad = models.IntegerField(null=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.SET_NULL, null=True)
    vacunado = models.ForeignKey(Vacunado, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(null=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} Entidad : {self.entidad}, Estado: {self.vacunado}, apellido: {self.apellido}'
