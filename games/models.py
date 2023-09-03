from django.db import models
from reviews.models import GAME_CHOICE

class Games(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=270)
    genero = models.CharField(max_length=50)
    edad = models.IntegerField()
    juego = models.CharField(
        max_length=50,
        choices=GAME_CHOICE,
        default="NADA",
    )

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ["nombre"]
        
