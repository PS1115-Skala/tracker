from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    id_user     = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    position    = models.CharField(max_length=20)
    description = models.CharField(max_length=200,default='Descripcion')
    genre_choice = (
        ('Maculino','M'),
        ('Femenino', 'F'),
        ('Otro','O'),
    )
    genre       = models.CharField(max_length=1, choices=genre_choice, default='Otro')

    def __str__(self):
        return ('\nPosicion: ' + self.position +
            '\nDescripcion: '+ self.description +
            '\nGenero: '+ self.genre
            )

class Activity(models.Model):
    title = models.CharField(max_length=80)
    start = models.DateField()
    end = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)