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
        extra_kwargs = {
            'url': {'view_name': 'apiapp:ingrediente-detail', 'lookup_field': 'id'}
        }

class IngredienteSerializer2(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedIdentityField(view_name='apiapp:ingrediente-detail')
    class Meta:
        model = Ingrediente
        fields = ['path']
        extra_kwargs = {
            'url': {'view_name': 'apiapp:ingrediente-detail', 'lookup_field': 'id'}
        }

class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = serializers.HyperlinkedRelatedField(
        queryset = Ingrediente.objects.all(),
        many = True,
        read_only = False,
        view_name = 'apiapp:ingrediente-detail',
        lookup_field='id')
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        extra_kwargs = {
            'url': {'view_name': 'apiapp:hamburguesa-detail', 'lookup_field': 'id'}
        }
