"""Modulo vistas"""
# pylint: disable=no-member
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.db.models import Count, Q
from django.utils import timezone
from django.http import Http404

from .forms import AtraccionForm, ClienteForm, EmpleadoForm, TiqueteForm, EstadoMaquinaForm
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

def agregar_estado_maquina(request, atraccion_id):
    """Vista estado maquina"""
    try:
        atraccion = Atraccion.objects.get(id=atraccion_id)
    except Atraccion.DoesNotExist as exc:
        raise Http404('La atracción no existe') from exc
    if request.method == 'POST':
        form = EstadoMaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_atracciones')
    else:
        form = EstadoMaquinaForm(initial={'atraccion': atraccion})
    return render(request, 'form_estado_maquina.html', {'form':form, 'atraccion': atraccion})

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

#Estadisticas
def estadisticas_avanzadas(request):
    """Vista de estadísticas"""
    atracciones = Atraccion.objects.annotate(
        total_tiquetes=Count('tiquete'),
        #total_ingresos=Sum('tiquete__precio')
    )
    return render(request, 'estadisticas.html', {'atracciones': atracciones})

#Control ocupación
def control_ocupacion(request):
    """Vista control ocupación"""
    ocupacion = Atraccion.objects.annotate(
        clientes_en_uso=Count(
            'tiquete',
            filter=Q(tiquete__fecha=timezone.localdate())
        )
    )
    return render(request, 'control_ocupacion.html', {'ocupacion': ocupacion})
