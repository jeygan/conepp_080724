from django.contrib import admin

from aplicaciones.productos.models import Productos,AsignacionDeProductos

# Register your models here.

admin.site.register(Productos)
admin.site.register(AsignacionDeProductos)