from django.db import models

# Create your models here.

class Trabajadores(models.Model):

    cargo =(
        ("geologo", "Geologo"), 
        ("especialista_auditor", "Especialista Auditor"), 
        ("tecnico_instrumentista", "Tecnico Instrumentista"), 
    ) 

    departamento =( 
        ("ingenieria", "Ingenieria "), 
        ("seguridad", "Seguridad"), 
        ("programacion_y_control", "Programacion y Control"), 
    ) 

    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre",max_length=255,null=True,blank=True)
    rut = models.IntegerField(blank=True, null=True,unique=True)
    cargo = models.CharField("Cargo",max_length=150,choices=cargo,default='geologo',blank=False, null=False)
    departamento = models.CharField("Departamento",max_length=150,choices=departamento,default='ingenieria',blank=False, null=False)
    
    #departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,blank=True, null=True)
    #departamento = models.CharField("Departamento",max_length=255,null=True,blank=True)
    #departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,blank=True, null=True)
    #descripcion = models.TextField(null=True,blank=True)
    

    
    def __str__(self):
        return f'Nombre: {self.nombre} Cargo: {self.cargo}'
    
    #El numero ya esta en usuarios
    #numero_telefono = models.CharField("Numero de telefono",max_length=30)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = '1.Trabajadores'
        db_table = 'Trabajadores'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
        ]   