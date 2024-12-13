"""Modulo vistas"""
# pylint: disable=no-member
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from .forms import AtraccionForm, ClienteForm, EmpleadoForm, TiqueteForm
from .models import Atraccion, Cliente, Empleado, Tiquete


#Vistas Agregar
def agregar_cliente(request):
    """Vista agregar cliente"""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'form_cliente.html', {'form':form})


def agregar_empleado(request):
    """Vista agregar empleado"""
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'form_empleado.html', {'form':form})

def agregar_atraccion(request):
    """Vista agregar atracciones"""
    if request.method == 'POST':
        form = AtraccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_atracciones')
    else:
        form = AtraccionForm()
    return render(request, 'form_atraccion.html', {'form':form})

def agregar_tiquete(request):
    """Vista agregar tiquete"""
    if request.method == 'POST':
        form = TiqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tiquetes')
    else:
        form = TiqueteForm()
    return render(request, 'form_tiquete.html', {'form':form})

#Vistas Edición
class ClienteUpdateView(UpdateView):
    """Edicion Cliente"""
    model = Cliente
    fields = ['nombre','cedula','telefono','correo','estatura',
              'edad','contacto_familiar','publicidad']
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('listar_clientes')

class EmpleadoUpdateView(UpdateView):
    """Edicion Empleado"""
    model = Empleado
    fields = '__all__'
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('listar_empleados')

class AtraccionUpdateView(UpdateView):
    """Edicion Atraccion"""
    model = Atraccion
    fields = '__all__'
    template_name = 'atraccion_form.html'
    success_url = reverse_lazy('listar_atracciones')

class TiqueteUpdateView(UpdateView):
    """Edicion Tiquete"""
    model = Tiquete
    fields = '__all__'
    template_name = 'tiquete_form.html'
    success_url = reverse_lazy('listar_tiquetes')

#Vistas Eliminación
class ClienteDeleteView(DeleteView):
    """Eliminacion Cliente"""
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('listar_clientes')

class EmpleadoDeleteView(DeleteView):
    """Eliminacion Empleado"""
    model = Empleado
    template_name = 'empleado_confirm_delete.html'
    success_url = reverse_lazy('listar_empleados')

class AtraccionDeleteView(DeleteView):
    """Eliminacon Atraccion"""
    model = Atraccion
    template_name = 'atraccion_confirm_delete.html'
    success_url = reverse_lazy('listar_atracciones')


class TiqueteDeleteView(DeleteView):
    """Eliminacion Tiquete"""
    model = Tiquete
    template_name = 'tiquete_confirm_delete.html'
    success_url = reverse_lazy('listar_tiquetes')






def home(request): # pylint: disable=unused-argument
    """Inicio"""
    return render(request, 'home.html')


def listar_clientes(request):
    """Lista clientes"""
    clientes = Cliente.objects.all() #Esto recupera todos los clientes
    return render(request, 'clientes.html',{'clientes': clientes})


def listar_empleados(request):
    """Lista empleados"""
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html',{'empleados':empleados})


def listar_atracciones(request):
    """Lista atracciones"""
    atracciones = Atraccion.objects.all()
    return render(request,'atracciones.html',{'atracciones':atracciones})


def listar_tiquetes(request):
    """Lista tiquetes"""
    tiquetes = Tiquete.objects.all()
    return render(request, 'tiquetes.html', {'tiquetes': tiquetes})
