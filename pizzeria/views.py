from django.shortcuts import render, HttpResponseRedirect
from pizzeria.models import Parking
import requests
import json
from pizzeria.forms import ParkingForm

def main(request):

    return render(request, "main.html")


def my_map(request):

    return render(request, "my_map.html")


def add_new_park(request):
    if request.method == 'POST':
        filled_form = ParkingForm(request.POST)
        parking = filled_form.save(commit=False)
        parkings = get_parkings(parking.Longitude, parking.Latitude)

        for park in parkings:
            if not Parking.objects.filter(Address = park["address"]).exists():
                new_park=Parking()
                new_park.Address = park["address"]
                new_park.Longitude = park["lng"]
                new_park.Latitude = park["lat"]
                new_park.save()

        return HttpResponseRedirect('/pizzeria/new_park')

    data = dict()
    data["location_form"] =  ParkingForm()
    return render(request, 'new_park.html', data)

def get_parkings(longitude, latitude):
    url = "http://api.parkwhiz.com/search/?lat=" + str(latitude)
    url += "&lng="+str(longitude)
    url += "&key=62d882d8cfe5680004fa849286b6ce20"

    response = requests.request('GET', url)
    print("$$$$ For {} RC is: {}".format(url, response.status_code))
    if response.status_code == 200:
        return response.json()["parking_listings"]