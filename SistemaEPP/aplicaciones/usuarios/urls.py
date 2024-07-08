from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views_class as VistasUsuarioClass
from . import views_function as VistasUsuarioDef

app_name ="usuarios"

urlpatterns = [


    path('perfil', VistasUsuarioClass.Perfil_Usuario.as_view(), name='perfil'),

    #Para registrar usuarios(de forma personalizada)
    path('registrarUsuario', VistasUsuarioClass.RegistroUsuario.as_view(), name='registrarUsuario'),
    path("listaUsuarios", VistasUsuarioClass.ListaUsuarios.as_view(), name="listaUsuarios"),
    
    
    path('editar/<slug:pk>', VistasUsuarioDef.usuarios_update, name='usuariosEditar'),
    path('perfil-usuario/<slug:pk>/', VistasUsuarioClass.PerfilDetailView.as_view() ,name="perfilUsuario"),
    path('<pk>/delete/', VistasUsuarioClass.UsuarioDeleteView.as_view() ,name="borrarUsuario"),
    path('cuentaCreada/', VistasUsuarioDef.UsuarioCuentaCreada ,name="cuentaCreada"),


    #path('login/', vistasLogin.Login.as_view() ,name="login"),
    
    #path('', views.index.as_view() ,name="index"),



    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)