from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasLogin

app_name ="login"

urlpatterns = [
    

    
    path('login/', vistasLogin.login ,name="login"),

    #Para registro de...
    #path('registroA/', vistasLogin.RegistroAlumno.as_view() ,name="registroAlumno"),

    #path('cuentaCreada/', vistasLogin.MensajeCuentaCreada.as_view() ,name="cuenta_creada"),

    path('logout/', vistasLogin.logout ,name="logout"),
    




    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)