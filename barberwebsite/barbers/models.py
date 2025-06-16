from django.db import models
from django.contrib.auth.models import User
from service.models import Service

# Create your models here.

class BarberInfo(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='barber_photos/', blank=True, null=True)
    bio = models.TextField()
    skills = models.TextField()
    reviews = models.TextField()
    services = models.ManyToManyField(Service, related_name='barbers')

    def __str__(self):
        return self.name
   

   
