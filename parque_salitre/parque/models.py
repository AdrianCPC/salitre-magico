"""Creacion de modelos"""
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models


class Cliente(models.Model):
    """Clientes del parque"""
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    estatura = models.FloatField(validators=[
        MinValueValidator(0, message="La estatura debe ser positiva.")
    ])
    edad = models.IntegerField(validators=[
        MinValueValidator(0, message="La edad no puede ser negativa."),
        ( MaxValueValidator(110, message="Edad no válida."))
    ])
    contacto_familiar = models.CharField(max_length=100, null=True, blank=True)
    publicidad = models.BooleanField(default=True)
    def __str__(self):
        return str(self.nombre)
    def clean(self):
        """Validación edad negativa"""
        if self.edad is not None:
            if self.edad < 0:
                raise ValidationError("La edad no puede ser negativa")
        super().clean()

class Empleado(models.Model):
    """Tipos empleados en el parque"""
    TIPOS_EMPLEADO = [
        ('ADMIN', 'Administrativo'),
        ('LOG', 'Logística'),
        ('PUB', 'Publicidad'),
        ('OPE', 'Operador'),
        ('MANT', 'Mantenimiento'),
    ]
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=15)
    tipo = models.CharField(max_length=5, choices=TIPOS_EMPLEADO)
    horario_laboral = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.tipo}"



class Atraccion(models.Model):
    """Atracciones del parque"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    clasificacion = models.CharField(max_length=50)
    estatura_minima = models.FloatField(validators=[
        MinValueValidator(0, message="La estatura mínima debe ser positiva.")
    ])
    condiciones_uso = models.TextField()
    estado = models.BooleanField(default=True) # True: Disponible, False: No disponible
    def __str__(self):
        return str(self.nombre)


class Tiquete(models.Model):
    """Tiquetes de ingreso"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    atraccion = models.ForeignKey(Atraccion, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Tiquete de {self.cliente} para {self.atraccion}"