from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.usuarios.models import Usuarios



###################### AQUI COMIENZAN LOS FORMULARIOS PARA TODO DE INVENTARIO ##########################################
'''
class CalidadForm(ModelForm):


    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(CalidadForm, self).__init__(*args, **kwargs)
        print("Formulario CalidadForm: \n")
        #print("usuario: ",self.usuarioID)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Calidad
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }


'''

class NewUserForm(UserCreationForm):

    class Meta:
        model = Usuarios
        fields = '__all__'


class UsuarioPersonalizadoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(UsuarioPersonalizadoForm, self).__init__(*args, **kwargs)
        print("Formulario UsuarioPersonalizado: \n")
        print("usuario: ",usuario_id)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Usuarios
        #fields = "__all__"

        #Estos campos no son necesarios en el registro normal de usuarios
        exclude = ('user_permissions','groups','last_login','activo','admin','is_superuser','imagenPerfil','password')
        widgets = {
            #"nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }



################## NUEVO FORMULARIO PARA ESTE SISTEMA ###################

class UsuarioFormModel(ModelForm):
    class Meta:
            model = Usuarios
            fields = ["username", "nombres", "apellidos", "password",'rol','activo']

#Esto es personalizado para la clave 
class UsuarioForm(forms.Form):

    rol =( 
        ("administrador", "Administrador "), 
        ("profesor", "Profesor"), 
    ) 

    estado =( 
        ("activo", "Activo "), 
        ("inactivo", "Inactivo"), 
    ) 
  
    #correo_electronico = forms.EmailField(label="Correo Electronico",widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico','class':'form-control'}))
    username = forms.EmailField(label="Usuario",widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'placeholder': 'Nombre','class':'form-control'}))
    apellido = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={'placeholder': 'Apellido','class':'form-control'}))
    rol = forms.ChoiceField(choices = rol,widget=forms.Select(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Contraseña",widget=forms.TextInput(attrs={'placeholder': 'Contraseña','class':'form-control'}))
    #password2 = forms.CharField(label="password2",widget=forms.TextInput(attrs={'placeholder': 'Repita Contrseña','class':'form-control'}))
    estado = forms.ChoiceField(choices = estado,widget=forms.Select(attrs={'class':'form-control'}))