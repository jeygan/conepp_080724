from dataclasses import fields
from rest_framework import serializers
from aplicaciones.usuarios.models import Estado,Municipio,Parroquia

#Aqui no vamos a establecer serializadores


#Serializaser para obtener los municipios
class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'
        #fields = ['digitos','repetidor'] #cuando son campos especificos
        
        #exclude

#Serializaser para obtener las parroquias
class ParroquiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquia
        fields = '__all__'
        #fields = ['digitos','repetidor'] #cuando son campos especificos