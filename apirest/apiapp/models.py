from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100, default='')
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100,  default='')
    imagen = models.CharField(max_length=100, default='')
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self): #cambiar para poder hacer la anidación y/o que imprima ingredientes = [{path: url}] 
        return self.nombre


