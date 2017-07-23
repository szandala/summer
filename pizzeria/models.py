from django.db import models

# Create your models here.

class Parking(models.Model):
    Address = models.CharField(max_length=255)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return self.Address