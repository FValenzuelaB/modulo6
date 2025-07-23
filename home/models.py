from django.db import models

# Create your models here.

class Fruta(models.Model):
    nombre=models.CharField("Nombre", max_length=40)
    color=models.CharField("Color", max_length=40)


    def __str__(self):
        return f"{self.nombre}"