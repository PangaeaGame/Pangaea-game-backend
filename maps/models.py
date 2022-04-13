from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Map(models.Model):
    coordX = models.IntegerField(null=False)
    coordY = models.IntegerField(null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('coordX', 'coordY')
