from django.db import models

# Create your models here.
class Divisions(models.Model):
    divisionname = models.CharField(max_length = 20)
    