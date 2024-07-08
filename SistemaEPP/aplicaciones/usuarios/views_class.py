from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.usuarios.form import UsuarioForm, UsuarioPersonalizadoForm

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

# Create your views here.

class Perfil_Usuario(TemplateView):

    template_name = "usuarios/perfil-usuario.html"

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

 
class ListaUsuarios(ListView):

    model=Usuarios
    template_name = "usuarios/lista-usuario.html"

    #Esta funcion es para personalizar la busqueda de usuarios
    def get_queryset(self):
        queryset = super(ListaUsuarios, self).get_queryset()
        return queryset.all()
    
    #Para agregar otros contextos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        context["form"] = UsuarioForm
        return context




class RegistroUsuario(View):
    form_class = UsuarioForm

    #Este initial solo sera durante las pruebas
    #initial = {"nombre": "pedro@gmail.com"}
    template_name = "usuarios/lista-usuario.html"

    #Para agregar otros contextos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        #context["object_list"] = Usuarios.objects.all()
        context["form"] = UsuarioForm
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class

        print("Entramos en get")
        return render(request, self.template_name, {"form": form,'usuario':self.request.user})

    def post(self, request, *args, **kwargs):

        print("ENTRAMOS EN POST")
        print(request.POST)
        #form = self.form_class(request.POST)
        #form = UsuarioForm(data=request.POST)
        

        #Verificamos que no haya correos repetidos
        if Usuarios.objects.filter(username=request.POST.get('username')).count()>0:

            print("ERROR username REPETIDO")
            return render(request, self.template_name, {"form": self.form_class,'MensajeCorreo':'Este correo_electronico ya existe' })
        #Aqui si no existe el correo carga todo normal
        else:

            usuario = Usuarios(
                correo_electronico=request.POST.get('username'),
                nombres=request.POST.get('nombre'),
                apellidos=request.POST.get('apellido'),
                rol=request.POST.get('rol'),
                activo=False,
                
            )


            usuario.set_password(request.POST.get('password1'))
            print("mostrando> ",usuario)
            usuario.save()

            return HttpResponseRedirect(reverse_lazy('usuarios:cuentaCreada'))
        
           

        return render(request, self.template_name, {"form": form})
    


#Estamos probando detalles con clases django
class PerfilDetailView(DetailView):
    # specify the model to use
    model = Usuarios
    template_name = 'usuarios/perfil-usuario.html'

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


class UsuarioDeleteView(DeleteView):
    # specify the model you want to use
    model = Usuarios
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('usuarios:listaUsuarios')
     
    template_name = "usuarios/borrar-usuario.html"











