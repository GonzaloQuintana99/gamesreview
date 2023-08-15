from django import forms

class RegisterForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=50, required=True)
    creador = forms.BooleanField(required=False)
