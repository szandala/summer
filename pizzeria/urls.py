__author__ = 'szandala'
from django.conf.urls import url
import pizzeria.views

urlpatterns = [
    url(r'^$', pizzeria.views.main),
    url(r'^map', pizzeria.views.my_map),
    url(r'^new_park', pizzeria.views.add_new_park)
]
