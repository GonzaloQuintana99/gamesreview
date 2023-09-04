from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
import datetime

from authmanager.models import Avatar

from django.contrib.auth.decorators import login_required

from django.contrib import messages

def reviews(req):
    ctx = {'reviews': Reviews.objects.all()}
    return render(req, "reviews/reviews.html", ctx)



def minecraft(req):
    patron = 'Minecraft'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def csgo(req):
    patron = 'Counter Strike Global Offensive'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def leagueoflegends(req):
    patron = 'League of Legends'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def terraria(req):
    patron = 'Terraria'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def rust(req):
    patron = 'Rust'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def valorant(req):
    patron = 'Valorant'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def phasmophobia(req):
    patron = 'Phasmophobia'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)

def gtav(req):
    patron = 'Grand Theft Auto V'
    game = Reviews.objects.filter(juego__icontains=patron)
    ctx = {"review": game}
    return render(req, "reviews/reviews.html", ctx)


def review(req, id_review):
    review = Reviews.objects.filter(id=id_review)
    avat = Avatar.objects.all()
    ctx = {"reviewc": review, 'avat': avat}
    return render(req, 'reviews/review.html', ctx)



@login_required
def editReview(req, id_review):
    review = Reviews.objects.get(id=id_review)
    usuario = req.user
    if usuario.username == review.creador:
        if req.method == "POST":
            miForm = EditReview(req.POST)
            if miForm.is_valid():
                review.titulo = miForm.cleaned_data.get('titulo')
                review.descripcion = miForm.cleaned_data.get('descripcion')
                review.review = miForm.cleaned_data.get('review')
                review.juego = miForm.cleaned_data.get('juego')
                review.save()
                return redirect(reverse_lazy('home'))
            else:
                miForm = EditReview(initial={
                'titulo': review.titulo,
                'descripcion': review.descripcion,
                'review': review.review,
                'juego': review.juego,
                'creador': review.creador
            })
            return render(req, 'reviews/reviewsFormEdit.html', {'form': miForm})
        else:
            miForm = EditReview(initial={
                'titulo': review.titulo,
                'descripcion': review.descripcion,
                'review': review.review,
                'juego': review.juego,
                'creador': review.creador
            })
        return render(req, 'reviews/reviewsFormEdit.html', {'form': miForm})
    else:
        messages.error(req, "¡No tienes permitido hacer eso!")
        return redirect(reverse_lazy('home'))

@login_required
def deleteReview(req, id_review):
    review = Reviews.objects.get(id=id_review)
    review.delete()
    return redirect(reverse_lazy('home'))

@login_required
def createReview(req):
    if req.method == "POST":
        miForm = CreateReview(req.POST)
        if miForm.is_valid():
            r_titulo = miForm.cleaned_data.get('titulo')
            r_descripcion = miForm.cleaned_data.get('descripcion')
            r_review = miForm.cleaned_data.get('review')
            r_juego = miForm.cleaned_data.get('juego')
            r_creador = miForm.cleaned_data.get('creador')
            review = Reviews(titulo=r_titulo,
                              descripcion=r_descripcion,
                              review=r_review,
                              juego=r_juego,
                              creador=r_creador,
                              )
            review.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = CreateReview()
    return render(req, 'reviews/reviewsForm.html', {'form': miForm})

def reviewsNew(req):
    mydate = datetime.date.today()
    # mydate.strftime('%m/%d/%Y')
    game = Reviews.objects.all()
    ctx = {"review": game, "mydate": mydate.strftime('%d-%m-%Y')}
    return render(req, 'reviews/reviewNew.html', ctx)