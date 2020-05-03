from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


#class IngredienteSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Ingrediente
    #    fields = '__all__'

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']
        ordering = ['id']
        extra_kwargs = {
            'url': {'view_name': 'apiapp:ingrediente-detail', 'lookup_field': 'id'}
        }

class EachIngredienteSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedIdentityField(view_name='apiapp:ingrediente-detail', lookup_field='id')
    class Meta:
        model = Ingrediente
        fields = ['path']
        extra_kwargs = {
            'url': {'view_name': 'apiapp:ingrediente-detail', 'lookup_field': 'id'}
        }


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = EachIngredienteSerializer(many=True, read_only=True)
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        ordering = ['id']
        extra_kwargs = {
            'url': {'view_name': 'apiapp:hamburguesa-detail', 'lookup_field': 'id'}
        }
