from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HamburguesaList, HamburguesaDetail, IngredienteList, IngredienteDetail, consulta_anidada, api_root
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    path('hamburguesa', HamburguesaList.as_view(), name='hamburguesa-list'),
    path('hamburguesa/<str:id>', HamburguesaDetail.as_view(), name='hamburguesa-detail'), 
    path('ingrediente', IngredienteList.as_view(), name='ingrediente-list'),
    path('ingrediente/<str:id>', IngredienteDetail.as_view(), name='ingrediente-detail'),
    path('hamburguesa/<str:id_ham>/ingrediente/<str:id_ing>', consulta_anidada),
    path('', api_root),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
app_name = 'apiapp'