"""URLS de todas las rutas de vistas"""
from django.urls import path
from . import views
from .views import (
    ClienteUpdateView, ClienteDeleteView,
    EmpleadoUpdateView, EmpleadoDeleteView,
    AtraccionUpdateView, AtraccionDeleteView,
    TiqueteUpdateView, TiqueteDeleteView
)

urlpatterns = [
    path('', views.home, name='home'), #Inicio ruta
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('atracciones/', views.listar_atracciones, name='listar_atracciones'),
    path('tiquetes/', views.listar_tiquetes, name='listar_tiquetes'),
    #URLS agregación de registros
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('atracciones/agregar/', views.agregar_atraccion, name='agregar_atraccion'),
    path('tiquetes/agregar/', views.agregar_tiquete, name='agregar_tiquete'),
    #URLS edicion y eliminar registros
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('empleado/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='editar_empleado'),
    path('empleado/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
    path('atraccion/editar/<int:pk>/', AtraccionUpdateView.as_view(), name='editar_atraccion'),
    path('atraccion/eliminar/<int:pk>/', AtraccionDeleteView.as_view(), name='eliminar_atraccion'),
    path('tiquete/editar/<int:pk>/', TiqueteUpdateView.as_view(), name='editar_tiquete'),
    path('tiquete/eliminar/<int:pk>/', TiqueteDeleteView.as_view(), name='eliminar_tiquete'),
]
