from django.db import models

# Create your models here.
class BusDetails(models.Model):
    Bus_No = models.IntegerField(unique=True)
    Departure_Time = models.TimeField()
    Destinations = models.CharField(max_length=500)
    Seats_Available = models.IntegerField()
    TicketsCosts = models.CharField(max_length=100)

