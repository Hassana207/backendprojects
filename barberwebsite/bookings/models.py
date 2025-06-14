from django.db import models
from django.contrib.auth.models import User
from service.models import Service
from barbers.models import BarberInfo 

# Create your models here.

class Booking(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    services = models.ManyToManyField(Service)
    barber = models.ForeignKey(BarberInfo,on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__ (self):
        return f"Booking by {self.customer.username} on {self.date}"
    
