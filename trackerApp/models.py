from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=60, validators=[EmailValidator(whitelist=['ubicutus.com'])])
    password = models.CharField(max_length=16)
    position = models.CharField(max_length=20)

    def __str__(self):
        return ('\nNombre: ' + self.first_name + ' ' + self.last_name +
            '\nCorreo: ' + self.email +
            '\nPosicion: ' + self.position
            )

class Activity(models.Model):
    title = models.CharField(max_length=80)
    start = models.DateField()
    end = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)