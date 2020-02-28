from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

# Create your models here.
class UserPosition(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
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
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)