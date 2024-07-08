from django.core.management.base import BaseCommand, CommandError

#Aqui esta el modelo de los Usuarios
from aplicaciones.usuarios.models import Usuarios

#Aqui esta el modelo para crear discipulos
from aplicaciones.usuarios.models import Discipulos
from aplicaciones.sucursales.models import Sucursales

class Command(BaseCommand):
    help = 'comando para crear usuarios de pruebas'

    def handle(self, *args, **options):


        #Creamos al usuario admin
        admin = Usuarios(username="admin",nombres="admin",apellidos="admin",email="admin@gmail.com",cedula="000000000",activo=True,is_superuser=True,admin=True,tipo_usuario="master",direccion="desconocido",sucursal=None,cobertura = None,telefono="00000000000")
        admin.set_password("admin")
        admin.save()


        #Creamos las sucursales de pruebas(antimano, las adjuntas, caricuao)
        sucursal_antimano = Sucursales.objects.create(nombre="antimano")
        sucursal_adjuntas = Sucursales.objects.create(nombre="adjuntas")
        sucursal_caricuao = Sucursales.objects.create(nombre="caricuao")

        #Creamos los usuarios de prueba

        #Los primeros tres usuarios son los pastores congregacionales

        #Usuario Warlis Zapata(pastor congregacional)
        warlis = Usuarios(username="warlis",nombres="warlis",apellidos="zapata",email="warlis@gmail.com",cedula="12322212",activo=True,is_superuser=False,admin=False,direccion="antimano",sucursal=sucursal_antimano,cobertura = None,telefono="04167156325")
        warlis.set_password("warlis")
        warlis.save()

        #Usuario Josue Arevalo
        josue = Usuarios(username="josue",nombres="josue",apellidos="arevalo",email="josue@gmail.com",cedula="11652212",activo=True,is_superuser=False,admin=False,direccion="las adjuntas",sucursal=sucursal_adjuntas,cobertura = None,telefono="04247156325")
        josue.set_password("josue")
        josue.save()

        #Usuario Luis Cedeño
        luis = Usuarios(username="luis",nombres="luis",apellidos="cedeño",email="luis@gmail.com",cedula="18676512",activo=True,is_superuser=False,admin=False,direccion="caricuao",sucursal=sucursal_caricuao,cobertura = None,telefono="04263356325")
        luis.set_password("luis")
        luis.save()



        #################################
        
        #Discipulos del pastor warlis
        hernan = Usuarios(username="hernan",nombres="hernan",apellidos="pineda",email="hernan@gmail.com",cedula="12322212",activo=True,is_superuser=False,admin=False,direccion="Ruiz Pineda",sucursal=sucursal_antimano,cobertura = warlis,telefono="04167156325")
        hernan.set_password("hernan")
        hernan.save()

        adixon = Usuarios(username="adixon",nombres="adixon",apellidos="laya",email="adixon@gmail.com",cedula="18952521",activo=True,is_superuser=False,admin=False,direccion="Maracao",sucursal=sucursal_antimano,cobertura = warlis,telefono="04265184674")
        adixon.set_password("adixon")
        adixon.save()

        anyelser = Usuarios(username="anyelser",nombres="anyelser",apellidos="perez",email="anyelser@gmail.com",cedula="24204625",activo=True,is_superuser=False,admin=False,direccion="antimano",sucursal=sucursal_antimano,cobertura = warlis,telefono="04242020470")
        anyelser.set_password("anyelser")
        anyelser.save()

        #Asignamos los discipulos al pastor warlis
        Discipulos.objects.create(sucursal=sucursal_antimano,pastor=warlis,discipulo=hernan)
        Discipulos.objects.create(sucursal=sucursal_antimano,pastor=warlis,discipulo=adixon)
        Discipulos.objects.create(sucursal=sucursal_antimano,pastor=warlis,discipulo=anyelser)



        ###################################
        """
        #Discipulos del pastor Josue
        hernan = Usuarios(username="hernan",nombres="hernan",apellidos="pineda",email="hernan@gmail.com",cedula="12322212",activo=True,is_superuser=False,admin=False,direccion="Ruiz Pineda",sucursal=sucursal_antimano,cobertura = warlis,telefono="04167156325")
        hernan.set_password("hernan")
        hernan.save()

        adixon = Usuarios(username="adixon",nombres="adixon",apellidos="laya",email="adixon@gmail.com",cedula="18952521",activo=True,is_superuser=False,admin=False,direccion="Maracao",sucursal=sucursal_antimano,cobertura = warlis,telefono="04265184674")
        adixon.set_password("adixon")
        adixon.save()

        anyelser = Usuarios(username="anyelser",nombres="anyelser",apellidos="perez",email="anyelser@gmail.com",cedula="24204625",activo=True,is_superuser=False,admin=False,direccion="antimano",sucursal=sucursal_antimano,cobertura = warlis,telefono="04242020470")
        anyelser.set_password("anyelser")
        anyelser.save()
        """


        ###################################

        
        
        
        self.stdout.write(self.style.HTTP_SUCCESS("USUARIOS CREADOS CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))