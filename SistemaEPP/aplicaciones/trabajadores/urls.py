from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views_class as VistaTrabajadoresClass
from . import views_function as VistaTrabajadoresDef

app_name ="trabajadores"

urlpatterns = [


    path('perfil', VistaTrabajadoresClass.PerfilTrabajador.as_view(), name='perfil'),

    #Para registrar usuarios(de forma personalizada)
    path('registrarTrabajador', VistaTrabajadoresClass.CrearTrabajador.as_view(), name='registrarTrabajador'),
    path("listaTrabajadores", VistaTrabajadoresClass.ListaTrabajadores.as_view(), name="listaTrabajadores"),
    
    
    path('editar/<slug:pk>', VistaTrabajadoresDef.trabajador_update, name='trabajadoresEditar'),
    path('perfil-trabajador/<slug:pk>/', VistaTrabajadoresClass.PerfilDetailView.as_view() ,name="perfilTrabajador"),
    path('<pk>/delete/', VistaTrabajadoresClass.TrabajadorDeleteView.as_view() ,name="borrarTrabajador"),
    path('cuentaCreada/', VistaTrabajadoresDef.trabajador_cuenta_creada ,name="cuentaCreada"),




    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)