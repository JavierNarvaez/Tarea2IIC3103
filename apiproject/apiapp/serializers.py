from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class IngredienteSerializerAux(serializers.HyperlinkedModelSerializer):
    ingrediente = IngredienteSerializer(required=False)
    class Meta:
        model = Ingrediente
        fields = ['url']

class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = serializers.HyperlinkedRelatedField(
        queryset = Ingrediente.objects.all(),
        many = True,
        read_only = False,
        view_name = 'apiapp:ingrediente_detail',
        lookup_field = 'id')
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
