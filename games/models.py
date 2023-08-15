from django.db import models

class Games(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=270)
    genero = models.CharField(max_length=50)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to ='static/uploads/')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ["nombre"]
        
