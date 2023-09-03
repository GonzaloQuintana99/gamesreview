from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_form(req):
    if req.method == "POST":
        miForm = AuthenticationForm(req, data=req.POST)
        if miForm.is_valid():
            username = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)

                try:
                    avatar = Avatar.objects.get(user=req.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    req.session["avatar"] = avatar

                messages.success(req, "Has iniciado sesión exitosamente.")
                return redirect(reverse_lazy('editProfile'))
            else:
                return render(req, 'authmanager/login.html', {'form': miForm})
        else:
            return render(req, 'authmanager/login.html', {'form': miForm})
    miForm = AuthenticationForm()
    return render(req, 'authmanager/login.html', {'form':miForm})

def users(req):
    context = {'avat': Avatar.objects.all()}
    return render(req, "authmanager/user_list.html", context)

def register(req):
    if req.method == "POST":
        miForm = RegisterForm(req.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return redirect(reverse_lazy('login'))
    else:
        miForm = RegisterForm()
    return render(req, 'authmanager/register.html', {'form': miForm})

@login_required
def editProfile(req):
    usuario = req.user
    if req.method == "POST":
        miForm = UserEditForm(req.POST, req.FILES)
        if miForm.is_valid():
            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[0].delete()
            
            avatar = Avatar(user= usuario, imagen=miForm.cleaned_data['imagen'])

            usuario.email = miForm.cleaned_data.get('email')
            usuario.password1 = miForm.cleaned_data.get('password1')
            usuario.password2 = miForm.cleaned_data.get('password2')
            usuario.first_name = miForm.cleaned_data.get('first_name')
            usuario.last_name = miForm.cleaned_data.get('last_name')
            usuario.save()
            avatar.save()

            imagen = Avatar.objects.get(user=req.user.id).imagen.url
            req.session["avatar"] = imagen
            return redirect(reverse_lazy('home'))
        else:
            return render(req, 'authmanager/editProfile.html', {'form': miForm, 'usuario': usuario.username})
    else:
        miForm = UserEditForm(instance=usuario)
    return render(req, 'authmanager/editProfile.html', {'form': miForm, 'usuario': usuario.username})