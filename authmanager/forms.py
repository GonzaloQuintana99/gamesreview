from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Ingresa tu Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    imagen = forms.ImageField(required= True)
    username = forms.CharField(label="Nombre de Usuario", disabled=True, required=False)
    email = forms.EmailField(label="Email", disabled=True, required=False)
    password1 = forms.CharField(label="Nueva Contraseña", widget= forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']