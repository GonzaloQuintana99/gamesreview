from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    creador = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["nombre"]
