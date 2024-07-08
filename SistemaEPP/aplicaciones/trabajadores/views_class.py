from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from aplicaciones.usuarios.models import Usuarios

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

from aplicaciones.trabajadores.models import Trabajadores
from aplicaciones.trabajadores.form import TrabajadorForm,TrabajadoresModelForm
# Create your views here.

class PerfilTrabajador(TemplateView):

    template_name = "trabajadores/perfil-trabajador.html"

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


class CrearTrabajador(CreateView):

    model = Trabajadores
    form_class = TrabajadoresModelForm
    context_object_name = 'trabajadores'
    template_name = "trabajadores/crear-trabajador.html"
    success_url = reverse_lazy('trabajadores:listaTrabajadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Peticion"

        print("prueba..")
        return context
    
 
class ListaTrabajadores(ListView):

    model=Usuarios
    template_name = "trabajadores/lista-trabajador2.html"

    #Esta funcion es para personalizar la busqueda de usuarios
    def get_queryset(self):
        queryset = super(ListaTrabajadores, self).get_queryset()
        return queryset.filter(rol="profesor")
    
    #Para agregar otros contextos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        context["form"] = TrabajadorForm()
        return context





#Estamos probando detalles con clases django
class PerfilDetailView(DetailView):
    # specify the model to use
    model = Usuarios
    template_name = 'profesores/perfil-profesor.html'

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


class TrabajadorDeleteView(DeleteView):
    # specify the model you want to use
    model = Usuarios

    #Esta funcion es para personalizar la busqueda de usuarios
    #def get_queryset(self):
    #    queryset = super(ProfesorDeleteView, self).get_queryset()
    #    return queryset.filter(rol="profesor")
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('trabajador:listaTrabajadores')
     
    template_name = "trabajador/borrar-trabajador.html"











