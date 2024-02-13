from django.db import models

from division.models import Divisions
from district.models import Districts

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length = 20)
    div_id = models.ForeignKey(Divisions,models.CASCADE)
    dis_id = models.ForeignKey(Districts,models.CASCADE)
