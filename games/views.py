from django.shortcuts import render
from .models import *

def games(req):
    context = {'games': Games.objects.all() }
    return render(req, "games/games.html", context)