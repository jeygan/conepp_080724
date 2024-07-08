from itertools import chain
import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from aplicaciones.localidad.models import Municipio, Parroquia
from aplicaciones.usuarios.api.serializers import MunicipiosSerializer, ParroquiasSerializer
from aplicaciones.usuarios.models import Usuarios




class set_encoder(json.JSONEncoder):
  def default(self, obj):
    return list(obj)




@api_view(['GET','POST'])
def crear_usuarios_api_view(request):


    if request.method == 'GET':
        #Datos que enviaremos
        print("Entramos aqui...")
        data = {'mensaje':'recibido'}
        return JsonResponse(data,safe = False)
    #    jugadas = Jugada.objects.all()
    #    jugadas_serializer = JugadaSerializer(jugadas,many=True)
    #    return Response(jugadas_serializer.data)
    
    if request.method == 'POST':

        #print("datos",request.data, "Usuario: ",request.user.username, " Id:",request.user.id)
        #print("datos tipos:  ",request.data.get('tipos'))
        print("datos",request.data)
        id_usuario = request.data.get('user_id')

        #Probando diccionario
        

        #Esto es para verificar cual es el id del usuario
        if id_usuario is None:
            print("El id es none aqui... no pasa nada")
        else:
            request.user = Usuarios.objects.get(id=int(id_usuario))
        
        print("Estas autenticado GENIAL",request.user)
        print("Permisos: ",request.user.get_all_permissions())
        #Asignamos los permisos del usuario
        datos = request.user.get_all_permissions()
        print("\n")
        print("\n")
            
        print("Estamos en la api de consultarPermisos:")
        print("Permisos de este usuario: ",datos)
        print("El tipo de dato es: ",type(datos))

        print("----------After converting set to json-----------")
        json_data = set_encoder().encode(datos)
        print("Codificado: ",json_data)
        print(type(json_data))


        print("\n")
        print("\n---------------------------------------")


        #print(jugadas_serializer.data)
        
        return HttpResponse(json_data)
        return JsonResponse(json_data,safe = False)
    


@api_view(['GET','POST'])
def get_municipios_api_view(request,id):


    if request.method == 'GET':
        #Datos que enviaremos
        data = {'mensaje':'recibido'}
        print("Entramos aqui en obtener municipios, id del estado: ",id)
        municipios = Municipio.objects.filter(id_estado_id=id)
        print(municipios)
        municipios_serializer = MunicipiosSerializer(municipios,many=True)

        #return JsonResponse(data,safe = False)
        return JsonResponse(municipios_serializer.data,safe = False)
    #    jugadas = Jugada.objects.all()
    #    jugadas_serializer = JugadaSerializer(jugadas,many=True)
    #    return Response(jugadas_serializer.data)
    
    if request.method == 'POST':

        #print("datos",request.data, "Usuario: ",request.user.username, " Id:",request.user.id)
        #print("datos tipos:  ",request.data.get('tipos'))
        print("datos",request.data)
        id_usuario = request.data.get('user_id')

        #Probando diccionario
        

        #Esto es para verificar cual es el id del usuario
        if id_usuario is None:
            print("El id es none aqui... no pasa nada")
        else:
            request.user = Usuarios.objects.get(id=int(id_usuario))
        
        print("Estas autenticado GENIAL",request.user)
        print("Permisos: ",request.user.get_all_permissions())
        #Asignamos los permisos del usuario
        datos = request.user.get_all_permissions()
        print("\n")
        print("\n")
            
        print("Estamos en la api de consultarPermisos:")
        print("Permisos de este usuario: ",datos)
        print("El tipo de dato es: ",type(datos))

        print("----------After converting set to json-----------")
        json_data = set_encoder().encode(datos)
        print("Codificado: ",json_data)
        print(type(json_data))


        print("\n")
        print("\n---------------------------------------")


        #print(jugadas_serializer.data)
        
        return HttpResponse(json_data)
        return JsonResponse(json_data,safe = False)
        

@api_view(['GET','POST'])
def get_parroquias_api_view(request,id):


    if request.method == 'GET':
        #Datos que enviaremos
        data = {'mensaje':'recibido'}
        print("Entramos aqui en obtener parroquias, id del municipio: ",id)
        parroquia = Parroquia.objects.filter(id_municipio=id)
        print(parroquia)
        parroquia_serializer = ParroquiasSerializer(parroquia,many=True)

        #return JsonResponse(data,safe = False)
        return JsonResponse(parroquia_serializer.data,safe = False)
    #    jugadas = Jugada.objects.all()
    #    jugadas_serializer = JugadaSerializer(jugadas,many=True)
    #    return Response(jugadas_serializer.data)
    