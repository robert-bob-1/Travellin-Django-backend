from django.db import models

# Create your models here.
class Destination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    pricePerNight = models.DecimalField(max_digits=10, decimal_places=2)
    totalSpots = models.IntegerField()
    sale = models.DecimalField(max_digits=3, decimal_places=1, default=0)

class Reservation(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    creationDate = models.DateField(auto_now_add=True)
    checkIn = models.DateField()
    checkOut = models.DateField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)