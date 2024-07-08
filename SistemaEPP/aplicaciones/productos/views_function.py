from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.usuarios.form import UsuarioFormModel
from aplicaciones.productos.form import ProductosModelForm

# Create your views here.


# update view for details@login_required
def producto_update(request, **kwargs):
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
        return redirect('productos:listaProductos')
    
    #Pasamos aqui cuando es GET
    return render(request, 'productos/editar-producto.html', context)

#Esta vista es para que no se envien 2 registros de usuarios
def producto_cuenta_creada(request):

    #verificamos que estamos logeados
    if request.user.is_authenticated:
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            form = ProductosModelForm
            contexto = {'form': form,
                        'object_list': Usuarios.objects.filter(rol="profesor"),
                        'usuario': request.user}
            
            #contexto['contrato'] ="SIN CONTRATO"
        

    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')
    
    return render(request, 'profesores/lista-profesor.html', contexto)


