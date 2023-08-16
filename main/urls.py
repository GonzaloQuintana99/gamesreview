from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('main/search/', search, name="search"),
]