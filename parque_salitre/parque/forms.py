"""Creación de formularios"""
from django import forms
from .models import Cliente, Empleado, Atraccion, Tiquete

#Creacion de los formularios
class ClienteForm(forms.ModelForm):
    """Formulario Cliente"""
    class Meta:
        model = Cliente
        fields = '__all__' #Inclusion de todos los campos en modelo cliente

class EmpleadoForm(forms.ModelForm):
    """Formulario Empleado"""
    class Meta:
        model = Empleado
        fields = '__all__'

class AtraccionForm(forms.ModelForm):
    """Formulario Atraccion"""
    class Meta:
        model = Atraccion
        fields = '__all__'

class TiqueteForm(forms.ModelForm):
    """Formulario Tiquete"""
    class Meta:
        model = Tiquete
        fields = '__all__'