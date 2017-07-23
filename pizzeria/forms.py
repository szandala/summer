__author__ = 'szandala'

from django.forms import ModelForm
from pizzeria.models import Parking

class ParkingForm(ModelForm):
    class Meta:
        model = Parking
        fields = ('Latitude', 'Longitude')