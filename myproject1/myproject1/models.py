from django.db import models

class About(models.Model):
    u_name = models.CharField(max_length=500)
    dob = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    no_exp = models.CharField(max_length=500)
    no_happy_customers = models.CharField(max_length=500)
    no_project_finished = models.CharField(max_length=500)
    no_digital_awards = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    date_time = models.CharField(max_length=5000)
    v_c = models.CharField(max_length=5000)
    v_status = models.CharField(max_length=10)

class companies(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to ="images/")