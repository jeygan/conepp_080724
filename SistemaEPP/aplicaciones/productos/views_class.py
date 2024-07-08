from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from aplicaciones.usuarios.models import Usuarios

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

from aplicaciones.trabajadores.models import Trabajadores
from aplicaciones.trabajadores.form import TrabajadorForm,TrabajadoresModelForm
from aplicaciones.productos.models import Productos
from aplicaciones.productos.form import ProductosModelForm
# Create your views here.

class PerfilProducto(TemplateView):

    template_name = "productos/perfil-producto.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("usuario permisos: ",request.user.get_all_permissions())
            #Aqui verificamos si el usuario esta activo para que ingrese
            ''' 
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
            '''


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        #context['informacion'] = "Hola..."

       
        context['usuario'] = self.request.user
        #context['contrato'] = Contrato.objects.get(usuario=self.request.user)
        context['contrato'] = "Sin contrato"
        print("en contextos:",context['contrato'])
        return context


class CrearProducto(CreateView):

    model = Productos
    form_class = ProductosModelForm
    context_object_name = 'productos'
    template_name = "productos/crear-producto.html"
    success_url = reverse_lazy('productos:listaProductos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Peticion"

        print("prueba..")
        return context
    
 
class ListaProductos(ListView):

    model=Productos
    template_name = "Productos/lista-producto.html"

    #Esta funcion es para personalizar la busqueda de usuarios
    def get_queryset(self):
        queryset = super(ListaProductos, self).get_queryset()
        return queryset.all()
    
    #Para agregar otros contextos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        context["form"] = ProductosModelForm()
        return context





#Estamos probando detalles con clases django
class PerfilDetailView(DetailView):
    # specify the model to use
    model = Productos
    template_name = 'productos/perfil-producto.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PerfilDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["usuario"] = self.request.user

        return context
    

"""
class UsuarioUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Usuarios 
  
    # specify the fields 
    fields = [ 
        "username", 
        "nombres",
        "apellidos",
        "contras"
    ] 
  
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url = reverse_lazy('usuarios:listaUsuarios')
"""


class ProductoDeleteView(DeleteView):
    # specify the model you want to use
    model = Usuarios

    #Esta funcion es para personalizar la busqueda de usuarios
    #def get_queryset(self):
    #    queryset = super(ProfesorDeleteView, self).get_queryset()
    #    return queryset.filter(rol="profesor")
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('productos:listaProductos')
     
    template_name = "productos/borrar-producto.html"











