from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views_class as VistaProductosClass
from . import views_function as VistaProductosDef

app_name ="productos"

urlpatterns = [


    path('perfil', VistaProductosClass.PerfilProducto.as_view(), name='perfil'),

    #Para registrar usuarios(de forma personalizada)
    path('registrarProducto', VistaProductosClass.CrearProducto.as_view(), name='registrarProducto'),
    path("listaProductos", VistaProductosClass.ListaProductos.as_view(), name="listaProductos"),
    
    
    path('editar/<slug:pk>', VistaProductosDef.producto_update, name='productosEditar'),
    path('perfil-producto/<slug:pk>/', VistaProductosClass.PerfilDetailView.as_view() ,name="perfilProducto"),
    path('<pk>/delete/', VistaProductosClass.ProductoDeleteView.as_view() ,name="borrarProducto"),
    path('cuentaCreada/', VistaProductosDef.producto_cuenta_creada ,name="cuentaCreada"),




    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)