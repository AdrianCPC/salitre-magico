"""Creacion de modelos"""

from django.db import models
#from django.core.validators import MinValueValidator, MaxValueValidator

class Cliente(models.Model):
    """Clientes del parque"""
    #...
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    estatura = models.FloatField()
    edad = models.IntegerField()
    contacto_familiar = models.CharField(max_length=100, null=True, blank=True)
    publicidad = models.BooleanField(default=True)
    def __str__(self):
        return str(self.nombre)


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
    def __str__(self): # pylint: disable=E1101
        return f"{self.nombre} - {self.get_tipo_display()}"



class Atraccion(models.Model):
    """Atracciones del parque"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    clasificacion = models.CharField(max_length=50)
    estatura_minima = models.FloatField()
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