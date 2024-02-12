from django.db import models

from division.models import Divisions

# Create your models here.

class Districts(models.Model):
    Districtname = models.CharField(max_length = 20)
    div_id = models.ForeignKey(Divisions,models.CASCADE)
