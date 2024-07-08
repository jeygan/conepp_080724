from django.core.management.base import BaseCommand, CommandError

#Aqui estan los ministerios
from aplicaciones.ministerios.models import Ministerios


class Command(BaseCommand):
    help = 'comando para crear los ministerios'

    def handle(self, *args, **options):


        print("VAMOS A CREAR LOS MINISTERIOS...")

        Ministerio_administradores = Ministerios.objects.create(nombre="administradores")
        Ministerio_ninos = Ministerios.objects.create(nombre="niños")
        Ministerio_prea = Ministerios.objects.create(nombre="prea")
        Ministerio_films = Ministerios.objects.create(nombre="films")
        Ministerio_servidores = Ministerios.objects.create(nombre="servidores")
        Ministerio_esformi = Ministerios.objects.create(nombre="esformi")
        Ministerio_alabanza_y_adoracion = Ministerios.objects.create(nombre="alabanza y adoracion")
        Ministerio_interseccion = Ministerios.objects.create(nombre="interseccion")
        Ministerio_produccion = Ministerios.objects.create(nombre="produccion")
        Ministerio_discipulado = Ministerios.objects.create(nombre="discipulado")
        Ministerio_familia = Ministerios.objects.create(nombre="familia")

         
        self.stdout.write(self.style.HTTP_SUCCESS("MINISTERIOS CREADOS CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))