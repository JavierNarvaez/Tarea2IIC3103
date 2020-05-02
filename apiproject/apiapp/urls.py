from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import hamburguesa_list, hamburguesa_detail, ingrediente_list, ingrediente_detail, consulta_anidada





urlpatterns=[
    path('hamburguesa', hamburguesa_list, name='hamburguesa_list'),
    path('hamburguesa/<str:_id>', hamburguesa_detail, name='hamburguesa_detail'), 
    path('ingrediente', ingrediente_list, name='ingrediente_list'),
    path('ingrediente/<str:_id>', ingrediente_detail, name='ingrediente_detail'),
    path('hamburguesa/<str:id_ham>/ingrediente/<str:id_ing>', consulta_anidada),
]

app_name = 'apiapp'