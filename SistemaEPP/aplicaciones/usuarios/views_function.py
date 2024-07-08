from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.usuarios.form import UsuarioForm, UsuarioFormModel

# Create your views here.


# update view for details@login_required
def usuarios_update(request, **kwargs):
    # recuperamos el objeto a actualizar
    #pk = Usuarios.objects.get(pk=kwargs.get('pk'))
    pk = kwargs.get('pk')

    print("valor es: ",pk)
    usuario = Usuarios.objects.get(pk=pk)
    # inicializamos el formulario con el objeto recuperado
    print("PROBANDO GET")
    form = UsuarioFormModel(request.POST or None,instance=usuario)
    
    userId = int(pk)
    context = {'usuario': request.user, 'form': form,'usuarioId':userId}
    if request.POST and form.is_valid():

        print("Probando save")
        form.save()
        return redirect('usuarios:listaUsuarios')
    
    #Pasamos aqui cuando es GET
    return render(request, 'usuarios/editar-usuario.html', context)

#Esta vista es para que no se envien 2 registros de usuarios
def UsuarioCuentaCreada(request):

    #verificamos que estamos logeados
    if request.user.is_authenticated:
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("ENTRAMOS EN GET DE CUENTAS CREADAS USUARIOS")
            form = UsuarioForm
            contexto = {'form': form,
                        'object_list': Usuarios.objects.all(),
                        'usuario': request.user}
            contexto['contrato'] ="SIN CONTRATO"
        

    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')
    
    return render(request, 'usuarios/lista-usuario.html', contexto)































"""
def registrarUsuarioPersonalizado(request):

    #verificamos que estamos logeados
    if request.user.is_authenticated:
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("ENTRAMOS EN GET PARA CREAR LA PETICION")
            form = UsuarioPersonalizadoForm(usuario=request.user)
            contexto = {'form': form,
                        ''
                        'user': request.user}
            contexto['contrato'] ="SIN CONTRATO"

            






        #Metodo(POST)
        else:

            #print(request.POST)
            print("\nEntramos en POST de registrar usuario\n")
            print(request.POST)
            form = UsuarioPersonalizadoForm(data=request.POST,usuario=request.user)

            #Variables para guardar
            #productos = request.POST.getlist('productos')
            #calidad = request.POST.getlist('calidad')
            #cantidad = request.POST.getlist('cantidad')
            
            #print(productos," jajajajaja")

            #si el formulario tiene los datos correctos entramos aqui
            
            
            
            #En caso de que el formulario sera correcto
            if form.is_valid():
            # and trabajo.is_valid() and suministro.is_valid():
            
            
                print("\nEl formulario es correcto")





                return redirect('peticiones:PeticionListar')
                #print("entramos aqui en POST")
                #orden = form.save()
                #orden_creada = orden.save(commit=False)
                #print("ORDEN CREADA:",orden_creada)
                #print(orden_creada.id)
                #print(orden_creada.observacion)
                #orden_creada.save()
            
                #print(suministro.cleaned_data)

                
            #    contexto = {'user': request.user,
            #                }
                
            
            
            
            else:

                print("la orden no fue creada...")
                
            # redirect to a new URL:
            print("Probando aqui......")
            return render(request, 'usuarios/usuario-crear.html',contexto)
    
    
    
    
    #Si el usuario no esta autenticado
    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')


    #print(contexto)
    return render(request, 'usuarios/usuario-crear.html', contexto)
"""