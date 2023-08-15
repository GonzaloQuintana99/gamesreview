from django.urls import path, include
from .views import *

urlpatterns = [
    path('games/', games, name="games"),
]