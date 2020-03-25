
import os
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files import File
from datetime import datetime

# Create your models here.
class UserData(models.Model):

    id_user     = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    position    = models.CharField(max_length=20)
    description = models.CharField(max_length=200,default='Descripcion')
    genre_choice = (
        ('Masculino','M'),
        ('Femenino', 'F'),
        ('Otro','O'),
    )
    genre       = models.CharField(max_length=9, choices=genre_choice, default='Otro')
    profileImage=models.ImageField( default= '/profileImages/default.jpg',upload_to="profileImages")
  

    def __str__(self):
        return (
            '\nUsuario: ' + self.id_user.username +
            '\nPosicion: ' + self.position +
            '\nDescripcion: '+ self.description +
            '\nGenero: '+ self.genre

            )
    def eraseOldMedia(self):
              
        if('default.jpg' not in self.profileImage.name):        
            eraseAddress= os.path.join(getattr(settings, 'MEDIA_ROOT', None),self.profileImage.name)
            os.remove(eraseAddress)

    def imageVerification(self):
        name=self.profileImage.name
        splitted=name.split(".")
        extension=splitted[len(splitted)-1]
        if(extension=="jpg" or extension=="png" or extension=="jpeg"):
            return True
        return False

        
class Activity(models.Model):
    title = models.CharField(max_length=80)
    start = models.DateTimeField()
    end = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        duration = (self.end - self.start)
        return (
            '\nTitulo: ' + self.title +
            '\n\tInicio: ' + self.start.strftime("%Y-%m-%d %H:%M:%S") +
            '\n\tFinal: ' + self.end.strftime("%Y-%m-%d %H:%M:%S") +
            '\n\tTotal: ' + str(duration.days) + ' days ' + str(duration.seconds) + ' seconds' +
            '\n\tUsuario: ' + self.id_user.__str__() + '\n'
        )

class LoanRequest(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(decimal_places=2, max_digits=15)
    loan_message = models.CharField(max_length=200)
    loan_date = models.DateTimeField()