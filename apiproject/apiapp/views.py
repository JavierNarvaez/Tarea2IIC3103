from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializer, IngredienteSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def hamburguesa_list(request):
    if request.method == 'GET':
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED) #{'Code': '201', 'Description': 'Hamburguesa creada'}
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # {'Code': '400', 'Description': 'Input inválido'}


@api_view(['GET', 'PATCH', 'DELETE'])
def hamburguesa_detail(request, _id):
    if not es_int(_id):
        return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        hamburguesa = Hamburguesa.objects.get(pk=_id)
    except ObjectDoesNotExist: 
        return Response({'Code': '404', 'Description': 'Hamburguesa inexistente'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = HamburguesaSerializer(hamburguesa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Code': '200', 'Description': 'Operación exitosa'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #{'Code': '400', 'Description': 'Parámetros inválidos'},

    elif request.method == 'DELETE':
        hamburguesa.delete()
        return Response({'Code': '200', 'Description': 'Hamburguesa eliminada'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def ingrediente_list(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #{'Code': '200', 'Description': 'Resultados obtenidos'}

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Code': '201', 'Description': 'Ingrediente creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #{'Code': '400', 'Description': 'Input inválido'}


@api_view(['GET', 'PATCH', 'DELETE'])
def ingrediente_detail(request, _id):
    if not es_int(_id):
        return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ingrediente = Ingrediente.objects.get(pk=_id)
    except ObjectDoesNotExist: 
        return Response({'code': '404', 'descripcion': 'Ingrediente inexistente'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data, status=status.HTTP_200_OK) #{'Code': '200', 'Description': 'Operación exitosa'},

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response({'Code': '200', 'Description': 'Ingrediente eliminado'}, status=status.HTTP_200_OK)



@api_view(['DELETE', 'PUT'])
def consulta_anidada(request, id_ham, id_ing):
    if not es_int(id_ham):
        return Response({'Code': '400', 'Description': 'id de hamburguesa inválido'}, status=status.HTTP_400_BAD_REQUEST)
    if not es_int(id_ing):
        return Response({'Code': '400', 'Description': 'id de ingrediente inválido'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        hamburguesa = Hamburguesa.objects.get(pk=id_ham)
    except ObjectDoesNotExist: 
        return Response({'Code': '404', 'Description': 'Hamburguesa inexistente'},status=status.HTTP_404_NOT_FOUND)

    try:
        ingrediente = Ingrediente.objects.get(pk=id_ing)
    except ObjectDoesNotExist: 
        return Response({'Code': '404', 'Description': 'Ingrediente inexistente'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE': ###REVISAR QUE ESTÉ EN LA HAMBURGUESA ANTES DE RETIRARLO
        hamburguesa.ingredientes.remove(ingrediente)
        return Response({'Code': '200', 'Description': 'Ingrediente retirado'}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        hamburguesa.ingredientes.add(ingrediente)
        return Response({'Code': '201', 'Description': 'Ingrediente agregado'}, status=status.HTTP_201_CREATED)



def es_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False
