from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static


app_name="eep"


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('aplicaciones.base_principal.urls')),
    path('', include(('aplicaciones.usuarios.urls'))),
    path('', include(('aplicaciones.login.urls'))),
    path('', include(('aplicaciones.trabajadores.urls'))),
    path('', include(('aplicaciones.productos.urls'))),
    #path('logout/', vistaLogin.Logout.as_view() ,name="logout"),

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""
    path('discipulado/', include('aplicaciones.discipulado.urls')),
    path('', include('aplicaciones.discipulado.api.urls')),
    path('', include('aplicaciones.servicio_congregacional.urls')),
    path('', include('aplicaciones.servicio_congregacional.api.urls')),
    path('', include('aplicaciones.base_principal.urls')),
    path('', include('aplicaciones.productos.urls')),
    path('', include('aplicaciones.ofertas.urls')),
    path('', include('aplicaciones.peticiones.urls')),
    path('', include(('aplicaciones.inventario_stock.urls'))),
    path('ministerios/', include(('aplicaciones.ministerios.urls'))),
    path('', include(('aplicaciones.sucursales.urls'))),
    path('', include(('aplicaciones.pdfs.urls'))),
    
    """