from django.shortcuts import render
from games.admin import *

def home(request):
    return render(request, "main/home.html")

def search(request):
    if request.GET['search']:
        patron = request.GET['search']
        games = Games.objects.filter(nombre__icontains=patron)
        context = {"games": games}
        return render(request, "main/search.html", context)
    return render(request, "main/home.html")