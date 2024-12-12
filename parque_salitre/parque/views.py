"""Modulo vistas"""
#from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Empleado, Atraccion, Tiquete


def home(request): # pylint: disable=unused-argument
    return render(request, 'home.html')

#Vista para listar clientes
def listar_clientes(request):
    clientes = Cliente.objects.all() #Esto recupera todos los clientes
    return render(request, 'clientes.html',{'clientes': clientes})

#Vista para lisatr empleados
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html',{'empleados':empleados})

#Vista para listar actracciones
def listar_atracciones(request):
    atracciones = Atraccion.objects.all()
    return render(request,'atracciones.html',{'atracciones':atracciones})

#Vista para listar tiquetes
def listar_tiquetes(request):
    tiquetes = Tiquete.objects.all()
    return render(request, 'tiquetes.html', {'tiquetes': tiquetes})
