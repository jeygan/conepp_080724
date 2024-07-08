from django.db import models

from aplicaciones.trabajadores.models import Trabajadores

# Create your models here.



class Productos(models.Model):

    

    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre",max_length=255,null=True,blank=True)
    descripcion = models.CharField("Descripcion",max_length=255,null=True,blank=True)
    cantidad = models.IntegerField(blank=True, null=True,unique=True)
    tipo = models.CharField("Tipo",max_length=255,null=True,blank=True)
    marca = models.CharField("Marca",max_length=255,null=True,blank=True)
    
    
    def __str__(self):
        return f'Producto: {self.nombre}'
    
    #El numero ya esta en usuarios
    #numero_telefono = models.CharField("Numero de telefono",max_length=30)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = '1.Productos'
        db_table = 'Productos'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
        ]   


class AsignacionDeProductos(models.Model):

    

    id = models.AutoField(primary_key=True)
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,blank=True, null=True)
    #producto = models.ForeignKey(Productos,on_delete=models.CASCADE,blank=True, null=True)


    fecha_asignacion = models.DateField(verbose_name='Fecha de Asignacion',blank=True,null=True)
    fecha_devolucion = models.DateField(verbose_name='Fecha de Devolucion',blank=True,null=True)
    estado = models.BooleanField(default=False)#Para verificar si esta activo o no 


    
    

    
    def __str__(self):
        return f'trabajador: {self.trabajador.nombre} Producto: {self.producto.nombre}'
    
    #El numero ya esta en usuarios
    #numero_telefono = models.CharField("Numero de telefono",max_length=30)

    class Meta:
        verbose_name = 'AsignacionDeProducto'
        verbose_name_plural = '2.AsignacionDeProductos'
        db_table = 'AsignacionDeProductos'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
        ]   