from django.contrib import admin
from .models import Cliente, Empleado, Atraccion, Tiquete
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Atraccion)
admin.site.register(Tiquete)
