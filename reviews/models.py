from django.db import models
from django.forms import ModelForm
from ckeditor.fields import RichTextField
import django.utils.timezone
import datetime

GAME_CHOICE = [
            ("NADA", "Selecciona un Juego"),
            ("Minecraft", "Minecraft"),
            ("League of Legends", "League of Legends"),
            ("Counter Strike Global Offensive", "Counter Strike Global Offensive"),
            ("Terraria", "Terraria"),
            ("Valorant", "Valorant"),
            ("Grand Theft Auto V", "Grand Theft Auto V"),
            ("Phasmophobia", "Phasmophobia"),
            ("Rust", "Rust"),
        ]

class Reviews(models.Model):
    
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    review = RichTextField()
    juego = models.CharField(
        max_length=50,
        choices=GAME_CHOICE,
        default="NADA",
    )
    creador = models.CharField(max_length=300, default="{{user.username}}")
    fecha = models.CharField(max_length=200, default=datetime.date.today().strftime('%d-%m-%Y'))

    def __str__(self):
        return f"{self.titulo}"
    
    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ["titulo"]
        

class CreateReview(ModelForm):
    class Meta:
        model = Reviews
        fields = ["titulo", "descripcion", "review", "juego", "creador"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["creador"].widget.attrs["readonly"] = True

class EditReview(ModelForm):
    class Meta:
        model = Reviews
        fields = ["titulo", "descripcion", "review", "juego", "creador"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["creador"].widget.attrs["readonly"] = True
