from django import forms
from django.forms import ModelForm
from .models import *
from django import forms

class LoginForm(forms.Form):
   email = forms.EmailField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())


class LoginUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['id','user','nombre','email','avatar','tipo']

class LoginVendedor(LoginUsuario):
    class Meta:
        model = Vendedor
        fields = ['id', 'user', 'nombre', 'email', 'avatar']


class LoginVendedorFijo(LoginVendedor):
    class Meta:
        model = vendedorFijo
        fields = ['id', 'user', 'nombre', 'email', 'avatar','horarioIni','horarioFin']

class LoginVendedorAmbulante(LoginVendedor):
    class Meta:
        model = vendedorAmbulante
        fields = ['id', 'user', 'nombre', 'email', 'avatar','activo']

class GestionProductosForm(forms.Form):
    idVendedor = 0
    nombre = forms.CharField(max_length=200)
    categoria = forms.IntegerField()
    descripcion = forms.CharField(max_length=500)
    stock = forms.IntegerField()
    precio = forms.IntegerField()


class editarProductosForm(ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre','categorias','descripcion','stock','precio','imagen']

class editarPerfilUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['user','nombre','email','avatar']

class editarPerfilVendedorFijo(editarPerfilUsuario):
    class Meta:
        model = vendedorFijo
        fields = ['id', 'user', 'nombre', 'email', 'avatar', 'horarioIni', 'horarioFin', 'formasDePago']

class editarPerfilVendedorAmbulante(editarPerfilUsuario):
    class Meta:
        model = vendedorAmbulante
        fields = ['id', 'user', 'nombre', 'email', 'avatar', 'activo', 'formasDePago']