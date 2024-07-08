#Para el login y logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

######## login con funciones ################

def login(request):

    print("Entramos aqui")
    form = AuthenticationForm()

    # Forma de agregarle estilos
    #form.fields['username'].label = "poder"
    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['username'].widget.attrs['placeholder'] = "Ingrese Username"
    form.fields['password'].widget.attrs['class'] = "form-control"
    form.fields['password'].widget.attrs['placeholder'] = "Ingrese Contraseña"
    #print(form)
    if request.method == "POST":

        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es valido entramos aqui
        if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                # Para verificar las credenciales del sistema
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    do_login(request, user)
                    
                    return HttpResponseRedirect(reverse_lazy('base_principal:index'))
                    #return redirect('/')

    return render(request, 'login.html', {'form':form})

#Cerramos sesion
def logout(request):

    print("Entramos aqui...")
    # Finalizamos la sesion
    do_logout(request)
    # Redireccionamos al inicio
    return redirect('/')
    

#####################################