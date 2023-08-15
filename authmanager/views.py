from django.shortcuts import render
from .models import *
from .forms import *

def login(req):
    # context = {'games': Auth.objects.all() }
    return render(req, "authmanager/login.html")

def register(request):
    if request.method == "POST":
        miForm = RegisterForm(request.POST)
        if miForm.is_valid():
            user_nombre = miForm.cleaned_data.get('nombre')
            user_appelido = miForm.cleaned_data.get('apellido')
            user_email = miForm.cleaned_data.get('email')
            user_password = miForm.cleaned_data.get('password')
            user_creador = miForm.cleaned_data.get('creador')

            user = User(nombre=user_nombre,
                        apellido=user_appelido,
                        email=user_email,
                        password=user_password,
                        creador=user_creador,
                        )
            user.save()
            return render(request, 'authmanager/login.html')
    else:
        miForm = RegisterForm()

    return render(request, "authmanager/register.html", {"form": miForm})