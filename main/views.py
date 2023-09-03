from django.shortcuts import render
from games.admin import *
from authmanager.admin import *
from reviews.admin import *

def home(request):
    context = {'avat': Avatar.objects.all(), "review": Reviews.objects.all()}
    return render(request, "main/home.html", context)

def search(request):
    if request.GET['search']:
        patron = request.GET['search']
        games = Games.objects.filter(nombre__icontains=patron)
        context = {"games": games}
        return render(request, "main/search.html", context)
    return render(request, "main/home.html")