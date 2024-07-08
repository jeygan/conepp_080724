from django.urls import path

from aplicaciones.usuarios.api.api import get_municipios_api_view, get_parroquias_api_view


urlpatterns = [

    #Normal

    #APIS PARA SOLICITAR DATA
    path('obtenerMunicipios/<int:id>/',get_municipios_api_view,name='obtenerMunicipios'),
    path('obtenerParroquias/<int:id>/',get_parroquias_api_view,name='obtenerParroquias'),
    
]