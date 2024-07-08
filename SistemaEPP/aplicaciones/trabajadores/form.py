from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.usuarios.models import Usuarios



#Aplicaciones de este proyecto
from aplicaciones.trabajadores.models import Trabajadores




################## NUEVO FORMULARIO PARA ESTE SISTEMA ###################

#Esto es personalizado para la clave 
class TrabajadorForm(forms.Form):

    cargo =(
        ("geologo", "Geologo"), 
        ("especialista_auditor", "Especialista Auditor"), 
        ("tecnico_instrumentista", "Tecnico Instrumentista"), 
    ) 

    departamento =( 
        ("ingenieria", "Ingenieria "), 
        ("seguridad", "Seguridad"), 
        ("programacion_y_control", "Programacion y Control"), 
    ) 
  
    #correo_electronico = forms.EmailField(label="Correo Electronico",widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico','class':'form-control'}))
    #username = forms.EmailField(label="Usuario",widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'placeholder': 'Nombre','class':'form-control'}))
    rut = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={'placeholder': 'Apellido','class':'form-control'}))
    cargo = forms.ChoiceField(choices = cargo,widget=forms.Select(attrs={'class':'form-control'}))
    departamento = forms.ChoiceField(choices = cargo,widget=forms.Select(attrs={'class':'form-control'}))
    
    
    #password1 = forms.CharField(label="Contraseña",widget=forms.TextInput(attrs={'placeholder': 'Contraseña','class':'form-control'}))
    #password2 = forms.CharField(label="password2",widget=forms.TextInput(attrs={'placeholder': 'Repita Contrseña','class':'form-control'}))
    #estado = forms.ChoiceField(choices = estado,widget=forms.Select(attrs={'class':'form-control'}))




class TrabajadoresModelForm(ModelForm):


    def __init__(self, *args, **kwargs):
        #curso_id = kwargs.pop('curso_id', None)
        super(ModelForm, self).__init__(*args, **kwargs)
        #print("id del curso:",curso_id)
        #self.fields['curso'].empty_label = None
        #self.fields['curso'].queryset = Cursos.objects.filter(id=curso_id)#.filter(sucursal=usuario_id.sucursal).exclude(username="admin")#Usuarios.objects.filter(id=self.usuarioID.id)

        #today = date.today()
        #self.fields['municipio'].empty_label = None
        #self.fields['estado'].queryset = Estado.objects.all()
        #self.fields['municipio'].queryset = Municipio.objects.none()
        #self.fields['parroquia'].queryset = Parroquia.objects.none()
        #self.fields['change_date'] = forms.DateField(initial=today, required=True,widget=DateInput(attrs={'type': 'date', 'style': 'width:200px'}))
        #self.fields['change_note'].widget = Textarea(attrs={'rows': '6', 'cols': '80'})
        #module_categories = Modules.objects.all().order_by('module_name').values_list('id', 'module_name')
        #self.fields['module_category'] = forms.CharField(label="Module Name", required=True,widget=forms.Select(choices=module_categories,attrs={'style': 'width: 300px;'}))
        #self.fields['form_name'] = forms.CharField(label="Form/Class Name", required=False, initial="", max_length=50)

    class Meta:

        model = Trabajadores
        #fields = "__all__"
        fields = ['nombre','rut','cargo','departamento']
        widgets = {
            "nombre": forms.TextInput(attrs={'placeholder': 'Ingrese Nombre','class':'form-control'}),
            "rut": forms.TextInput(attrs={'placeholder': 'Ingrese Nombre del RUT','class':'form-control'}),
            "cargo": forms.Select(attrs={'class':'form-control','style':''}),
            "departamento": forms.Select(attrs={'class':'form-control','style':''}),
                
                
                
        }