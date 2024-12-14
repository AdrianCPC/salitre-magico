"""Creación de pruebas unitarias"""
# pylint: disable=no-member
from django.forms import ValidationError
from django.test import TestCase
from .models import Atraccion, Cliente, EstadoMaquina

class ModelsTestCase(TestCase):
    """Atraccion"""
    def setUp(self):
        self.atraccion = Atraccion.objects.create(
            nombre="Montaña Rusa", descripcion="Alta velocidad", clasificacion="Adultos",
            estatura_minima=1.5, condiciones_uso="Sin problemas cardíacos", estado=True
        )

    def test_estado_maquina(self):
        """Estado maquina"""
        estado = EstadoMaquina.objects.create(
            atraccion=self.atraccion, estado="Disponible", observaciones="Todo en orden"
        )
        self.assertEqual(estado.estado, "Disponible")

class ViewsTestCase(TestCase):
    """Cliente"""
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Juan Pérez", cedula="12345678", telefono="3001234567", correo="juan@mail.com",
            estatura=1.8, edad=25, publicidad=True
        )

    def test_publicidad_menores(self):
        """Publicidad"""
        self.cliente.edad = 15
        self.cliente.publicidad = True
        with self.assertRaises(ValidationError):
            self.cliente.full_clean()  #Esto lanza validacion

