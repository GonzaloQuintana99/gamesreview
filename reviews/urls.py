from django.urls import path, include
from .views import *

urlpatterns = [
    path('reviews/', reviews, name="reviews"),

    path('reviews/Minecraft', minecraft, name="minecraft"),
    path('reviews/Counter Strike Global Offensive', csgo, name="csgo"),
    path('reviews/League of Legends', leagueoflegends, name="lol"),
    path('reviews/Terraria', terraria, name="terraria"),
    path('reviews/Rust', rust, name="rust"),
    path('reviews/Phasmophobia', phasmophobia, name="phasmophobia"),
    path('reviews/Valorant', valorant, name="valorant"),
    path('reviews/Grand Theft Auto V', gtav, name="gtav"),

    path('review/<id_review>', review, name="reviewc"),

    path('newreviews/', reviewsNew, name="newreviews"),

    path('edit_review/<id_review>', editReview, name="editreview"),
    path('delete_review/<id_review>', deleteReview, name="deletereview"),
    path('create_review/', createReview, name="createreview"),
]