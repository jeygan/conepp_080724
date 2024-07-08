from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group



#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

#Para las fechas
from datetime import datetime

    



class Index(TemplateView):

    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context["usuario"] = self.request.user
        return context
    




class IndexLogeado(TemplateView):

    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("Permisos: ",list(Permission.objects.all()))
            print("usuario: ",request.user," Cantidad de Grupos: ",Group.objects.all().count())
            #print("Permisos de usuario: ",request.user.get_all_permissions())
            #GCliente = Group.objects.get(name="cliente_E")

            #print("\n\n")
            #print("\n\nPermisos Grupo Productor: ",GProductor.permissions.all() )
            #for elemento in GCliente.permissions.all():
            #    print(elemento.name)
            #print("\n\n")

            #Grupo_productor.permissions.set(Permission.objects.get(name="Can add inventario"),
            #print("administrador:",request.user.groups.filter(name='administrador').exists())
            #print("productor:",request.user.groups.filter(name='productor').exists())
            #print("cliente :",request.user.groups.filter(name='cliente').exists())
            print("\n\n")
            
            
            fecha = datetime.now()
            print(fecha)
            #encontrado = Asistencia_del_dia.objects.filter(fecha_de_asistencia=fecha)

            #print(encontrado)
            
            #Aqui verificamos si el usuario esta activo para que ingrese
            ''' 
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
            '''

            #return redirect("src:index")
            #print("Usuario ",request.user)

            #Esto es algo que podria funcionar en algun momento
            #grupo="prueba"
            #print('Proyecto %s' % (grupo))

            

            
            #empresa_creada = Empresa.objects.filter(creado_por_id=request.user.id)


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context["usuario"] = self.request.user




        return context

