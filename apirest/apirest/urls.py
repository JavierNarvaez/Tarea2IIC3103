"""apirest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from apiapp.views import hamburguesa_list, hamburguesa_detail, ingrediente_list, ingrediente_detail, consulta_anidada


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamburguesa', hamburguesa_list),
    path('hamburguesa/<int:id>', hamburguesa_detail),
    path('ingrediente', ingrediente_list),
    path('ingrediente/<int:id>', ingrediente_detail),
    path('hamburguesa/<int:id>/ingrediente/<int:id>', consulta_anidada),
]
