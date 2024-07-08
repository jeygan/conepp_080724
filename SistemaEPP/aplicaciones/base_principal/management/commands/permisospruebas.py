from django.core.management.base import BaseCommand, CommandError

#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group

#Aqui esta el modelo de los Usuarios
from aplicaciones.usuarios.models import Usuarios

#Aqui esta el modelo para crear discipulos
from aplicaciones.usuarios.models import Discipulos
from aplicaciones.sucursales.models import Sucursales

class Command(BaseCommand):
    help = 'comando para crear usuarios de pruebas'

    def handle(self, *args, **options):

        # GRUPOS PARA:
        # pastores congregacionales,
        # pastores base, 
        # de ministerio 
        # de lider,
        # creyente


        #################################################

        #PROBANDO con grupo administrativo
        Grupo_administrador = Group.objects.get(name="administrador") #Permisos para administrador

        Grupo_administrador.permissions.add(

            #Permisos administrativos(para master)
            Permission.objects.get(name="Can view Sucursal"),
            Permission.objects.get(name="Can view Ministerio"),
        )

        #################################################

        #Aqui buscamos el grupo de permisos para pastor congregacional
        grupo_pastor_congregacional = Group.objects.get(name="pastor_congregacional")

        #Aqui buscamos el grupo de permisos para pastor base
        grupo_pastor_base = Group.objects.get(name="pastor_base")

        #Aqui buscamos el grupo de permisos para pastor de ministerio
        grupo_pastor_de_ministerio = Group.objects.get(name="pastor_ministerio")

        #Aqui buscamos el grupo de permisos para lideres
        grupo_lideres = Group.objects.get(name="lider")

        #Aqui buscamos el grupo de permisos para lideres
        grupo_creyentes = Group.objects.get(name="creyente")


        ##################################################################

        #Agregamos los permisos que tenga un pastor congregacional
        grupo_pastor_congregacional.permissions.add(

            #Permisos referente a las cosas de la congregacion y su inventario
            Permission.objects.get(name="Congregacional"), #sin este no se ven los de abajo
            Permission.objects.get(name="Can view inventario"), #inventario de su sucursal

            #Permisos referente a los discipulos
            Permission.objects.get(name="Modulo Discipulos"),
            Permission.objects.get(name="Agregar Discipulos"),
            Permission.objects.get(name="Lista Discipulos"),
            Permission.objects.get(name="Asistencia Discipulos"),

            #Permisos referente a los ministerios
            Permission.objects.get(name="Modulo Ministerios"),

            #Damos todos los permisos de ministerios(individuales)
            Permission.objects.get(name="Ministerio de Niños"),
            Permission.objects.get(name="Ministerio de Prea"),
            Permission.objects.get(name="Ministerios de Esformi"),
            Permission.objects.get(name="Ministerios de Alabanza"),
            Permission.objects.get(name="Ministerios de Discipulado"),
            Permission.objects.get(name="Ministerios de Produccion"),
            Permission.objects.get(name="Ministerios de Servidores"),
            Permission.objects.get(name="Ministerios de Interseccion"),
            Permission.objects.get(name="Ministerios de Familias"),



            #Permisos referentes a los productos que no se que son(creo que va enlazado a inventario)
            Permission.objects.get(name="Can view producto"),
            )
        
        #Agregamos los permisos que tenga un pastor base
        grupo_pastor_base.permissions.add(

            #Permisos referente a las cosas de la congregacion y su inventario
            Permission.objects.get(name="Congregacional"), #sin este no se ven los de abajo
            #Permission.objects.get(name="Can view inventario"), #inventario de su sucursal

            #Permisos referente a los discipulos
            Permission.objects.get(name="Modulo Discipulos"),
            Permission.objects.get(name="Agregar Discipulos"),
            Permission.objects.get(name="Lista Discipulos"),
            Permission.objects.get(name="Asistencia Discipulos"),

            #Permisos referente a los ministerios
            #Permission.objects.get(name="Modulo Ministerios"),

            #Damos todos los permisos de ministerios(individuales)
            #Permission.objects.get(name="Ministerio de Niños"),
            #Permission.objects.get(name="Ministerio de Prea"),
            #Permission.objects.get(name="Ministerios de Esformi"),
            #Permission.objects.get(name="Ministerios de Alabanza"),
            #Permission.objects.get(name="Ministerios de Discipulado"),
            #Permission.objects.get(name="Ministerios de Produccion"),
            #Permission.objects.get(name="Ministerios de Servidores"),
            #Permission.objects.get(name="Ministerios de Interseccion"),



            #Permisos referentes a los productos que no se que son(creo que va enlazado a inventario)
            #Permission.objects.get(name="Can view producto"),

            )


        #Agregamos los permisos que tenga un pastor de ministerio
        grupo_pastor_de_ministerio.permissions.add(


            #Permisos referente a los ministerios
            Permission.objects.get(name="Modulo Ministerios"),

            #Damos todos los permisos de ministerios(individuales)
            #Permission.objects.get(name="Ministerio de Niños"),
            #Permission.objects.get(name="Ministerio de Prea"),
            #Permission.objects.get(name="Ministerios de Esformi"),
            #Permission.objects.get(name="Ministerios de Alabanza"),
            #Permission.objects.get(name="Ministerios de Discipulado"),
            #Permission.objects.get(name="Ministerios de Produccion"),
            #Permission.objects.get(name="Ministerios de Servidores"),
            #Permission.objects.get(name="Ministerios de Interseccion"),


            )


        #Agregamos los permisos que tenga un lider
        grupo_lideres.permissions.add(

            #Permisos referente a las cosas de la congregacion y su inventario
            Permission.objects.get(name="Congregacional"), #sin este no se ven los de abajo
            #Permission.objects.get(name="Can view inventario"), #inventario de su sucursal

            #Permisos referente a los discipulos
            Permission.objects.get(name="Modulo Discipulos"),
            Permission.objects.get(name="Agregar Discipulos"),
            Permission.objects.get(name="Lista Discipulos"),
            Permission.objects.get(name="Asistencia Discipulos"),

            #Permisos referente a los ministerios
            #Permission.objects.get(name="Modulo Ministerios"),

            #Damos todos los permisos de ministerios(individuales)
            #Permission.objects.get(name="Ministerio de Niños"),
            #Permission.objects.get(name="Ministerio de Prea"),
            #Permission.objects.get(name="Ministerios de Esformi"),
            #Permission.objects.get(name="Ministerios de Alabanza"),
            #Permission.objects.get(name="Ministerios de Discipulado"),
            #Permission.objects.get(name="Ministerios de Produccion"),
            #Permission.objects.get(name="Ministerios de Servidores"),
            #Permission.objects.get(name="Ministerios de Interseccion"),

            )


        #Agregamos los permisos que tenga un creyente
        grupo_creyentes.permissions.add(

            #Permisos referente a las cosas de la congregacion y su inventario
            Permission.objects.get(name="Congregacional"), #sin este no se ven los de abajo
            #Permission.objects.get(name="Can view inventario"), #inventario de su sucursal

            #Permisos referente a los discipulos
            #Permission.objects.get(name="Modulo Discipulos"),
            #Permission.objects.get(name="Agregar Discipulos"),
            #Permission.objects.get(name="Lista Discipulos"),
            #Permission.objects.get(name="Asistencia Discipulos"),

            #Permisos referente a los ministerios
            #Permission.objects.get(name="Modulo Ministerios"),

            #Damos todos los permisos de ministerios(individuales)
            #Permission.objects.get(name="Ministerio de Niños"),
            #Permission.objects.get(name="Ministerio de Prea"),
            #Permission.objects.get(name="Ministerios de Esformi"),
            #Permission.objects.get(name="Ministerios de Alabanza"),
            #Permission.objects.get(name="Ministerios de Discipulado"),
            #Permission.objects.get(name="Ministerios de Produccion"),
            #Permission.objects.get(name="Ministerios de Servidores"),
            #Permission.objects.get(name="Ministerios de Interseccion"),

            )



        #Usuario Warlis Zapata
        warlis = Usuarios.objects.get(username="warlis")

        
        warlis.groups.add(grupo_pastor_congregacional)


        
        #Usuario Adixon Laya
        adixon = Usuarios.objects.get(username="adixon")
        
        
        adixon.groups.add(grupo_pastor_base)
        adixon.groups.add(grupo_pastor_de_ministerio) #En este caso es de familia

        #Agregamos para El, el ministerio de familia
        #usamos user_permissions.add para agregar un permiso
        adixon.user_permissions.add(Permission.objects.get(name="Ministerios de Familias"))
        

        ###################################

        
        
        
        self.stdout.write(self.style.HTTP_SUCCESS("PERMISOS CREADOS CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))