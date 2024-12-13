"""Creación de formularios"""
from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, Empleado, Atraccion, Tiquete

#Creacion de los formularios
class ClienteForm(forms.ModelForm):
    """Formulario Cliente"""
    class Meta:
        """Campos cliente"""
        model = Cliente
        fields = '__all__' #Inclusion de todos los campos en modelo cliente
    def clean_edad(self):
        """Edad escrita correctamente"""
        edad = self.cleaned_data.get('edad')
        if edad is None:
            raise ValidationError("La edad es obligatoria.")
        if edad < 0:
            raise ValidationError("La edad no puede ser negativa.")
        return edad
    def clean(self):
        cleaned_data = super().clean()
        edad = cleaned_data.get('edad')
        contacto_familiar = cleaned_data.get('contacto_familiar')
        if edad is not None and edad < 18 and not contacto_familiar:
            raise forms.ValidationError(
                "El contacto familiar es obligatorio para menores de 18 años")
        return cleaned_data

class EmpleadoForm(forms.ModelForm):
    """Formulario Empleado"""
    class Meta:
        """Campos empleado"""
        model = Empleado
        fields = '__all__'

class AtraccionForm(forms.ModelForm):
    """Formulario Atraccion"""
    class Meta:
        """Campos atraccion"""
        model = Atraccion
        fields = '__all__'

class TiqueteForm(forms.ModelForm):
    """Formulario Tiquete"""
    class Meta:
        """Campos tiquetes"""
        model = Tiquete
        fields = '__all__'