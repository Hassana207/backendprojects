from django.db import models
from django.contrib.auth.models import User
from service.models import Service
from barbers.models import BarberInfo 

# Create your models here.

class Bookings(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings')
    email = models.EmailField()
    services = models.ManyToManyField(Service)
    barber = models.ManyToManyField(BarberInfo)
    date = models.DateTimeField()

    def _str_ (self):
        return f"Booking by {self.customer.username} on {self.date}"
    
