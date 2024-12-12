from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #Inicio ruta
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('atracciones/', views.listar_atracciones, name='listar_atracciones'),
    path('tiquetes/', views.listar_tiquetes, name='listar_tiquetes'),
]
