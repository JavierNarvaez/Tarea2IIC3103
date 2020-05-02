from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status


from .models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializer, IngredienteSerializer

# Create your views here.

class HamburguesaViewSet(viewsets.ModelViewSet):
    serializer_class = HamburguesaSerializer
    queryset = Hamburguesa.objects.all()

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()

@api_view(['GET', 'POST'])
def hamburguesa_list(request):
    if request.method == 'GET':
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        return Response(serializer.data, status='200 Resultados obtenidos')

    elif request.method == 'POST':
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status='201 Hamburguesa creada')
        return Response(serializer.errors, status='400 Input inválido')

@api_view(['GET', 'PATCH', 'DELETE'])
def hamburguesa_detail(request, _id):
    #if para retornar '400 id invalido'
    try:
        hamburguesa = Hamburguesa.objects.get(pk=_id)
    except ObjectDoesNotExist: 
        return Response(status='404 Hamburguesa inexistente')

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = HamburguesaSerializer(hamburguesa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status='200 Operación exitosa')
        return Response(serializer.errors, status='400 Parámetros inválidos')

    elif request.method == 'DELETE':
        hamburguesa.delete()
        return Response(status='200 Hamburguesa eliminada')


@api_view(['GET', 'POST'])
def ingrediente_list(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data, status='200 Resultados obtenidos')

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status='201 Ingrediente creado')
        return Response(serializer.errors, status='400 Input inválido')

@api_view(['GET', 'PATCH', 'DELETE'])
def ingrediente_detail(request, _id):
    #if para retornar '400 id invalido'
    try:
        ingrediente = Ingrediente.objects.get(pk=_id)
    except ObjectDoesNotExist: 
        return Response(status='404 Ingrediente inexistente')

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = IngredienteSerializer(ingrediente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status='200 Operación exitosa')
        return Response(serializer.errors, status='400 Parámetros inválidos')

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response(status='200 Ingrediente eliminado')



@api_view(['DELETE', 'PUT'])
def consulta_anidada(request, id_ham, id_ing):
    if request.method == 'DELETE':
        pass

    elif request.method == 'PUT':
        hamburguesa = Hamburguesa.objects.get(pk=id_ham)
        ingrediente = Ingrediente.objects.get(pk=id_ing)


