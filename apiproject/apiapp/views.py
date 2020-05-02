from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.reverse import reverse


from .models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializer, IngredienteSerializer

# Create your views here.


class HamburguesaList(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED) #{'Code': '201', 'Description': 'Hamburguesa creada'}
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # {'Code': '400', 'Description': 'Input inválido'}



class HamburguesaDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get(self, request, *args, **kwargs):
        if not es_int(kwargs['id']):
            return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hamburguesa = Hamburguesa.objects.get(pk=kwargs['id'])
        except ObjectDoesNotExist: 
            return Response({'Code': '404', 'Description': 'Hamburguesa inexistente'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HamburguesaSerializer(hamburguesa, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK) #{'Code': '200', 'Description': 'Operación exitosa'},

    
    def patch(self, request, *args, **kwargs):
        if not es_int(kwargs['id']):
            return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hamburguesa = Hamburguesa.objects.get(pk=kwargs['id'])
        except ObjectDoesNotExist: 
            return Response({'Code': '404', 'Description': 'Hamburguesa inexistente'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HamburguesaSerializer(hamburguesa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Code': '200', 'Description': 'Operación exitosa'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #{'Code': '400', 'Description': 'Parámetros inválidos'},

    def delete(self, request, *args, **kwargs):
        if not es_int(kwargs['id']):
            return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hamburguesa = Hamburguesa.objects.get(pk=kwargs['id'])
        except ObjectDoesNotExist: 
            return Response({'Code': '404', 'Description': 'Hamburguesa inexistente'}, status=status.HTTP_404_NOT_FOUND)

        hamburguesa.delete()
        return Response({'Code': '200', 'Description': 'Hamburguesa eliminada'}, status=status.HTTP_200_OK)




class IngredienteList(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED) #{'Code': '201', 'Description': 'Hamburguesa creada'}
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # {'Code': '400', 'Description': 'Input inválido'}



class IngredienteDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def get(self, request, *args, **kwargs):
        if not es_int(kwargs['id']):
            return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ingrediente = Ingrediente.objects.get(pk=kwargs['id'])
        except ObjectDoesNotExist: 
            return Response({'Code': '404', 'Description': 'Ingrediente inexistente'}, status=status.HTTP_404_NOT_FOUND)

        serializer = IngredienteSerializer(ingrediente, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK) #{'Code': '200', 'Description': 'Operación exitosa'},

    def delete(self, request, *args, **kwargs):
        if not es_int(kwargs['id']):
            return Response({'Code': '400', 'Description': 'id inválido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ingrediente = Ingrediente.objects.get(pk=kwargs['id'])
        except ObjectDoesNotExist: 
            return Response({'Code': '404', 'Description': 'Ingrediente inexistente'}, status=status.HTTP_404_NOT_FOUND)

        ingrediente.delete()
        return Response({'Code': '200', 'Description': 'Ingrediente eliminado'}, status=status.HTTP_200_OK)



@api_view(['DELETE', 'PUT'])
def consulta_anidada(request, id_ham, id_ing, format=None):
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



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hamburguesas': reverse('hamburguesa-list', request=request, format=format),
        'ingredientes': reverse('ingrediente-list', request=request, format=format)
    })


def es_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False
