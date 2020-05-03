from django.db import models



class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

#    def __str__(self): #cambiar para poder hacer la anidación y/o que imprima ingredientes = [{path: url}]
#        path = 'http://localhost:8000/ingrediente/' ####CAMBIAAAAAAR
#        path += str(self.id)
 #       return 'path: %s' % (path)

class Hamburguesa(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True, related_name='hamburguesas')

   


