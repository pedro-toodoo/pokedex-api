from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pokemons.api import viewsets as pv

route = routers.DefaultRouter()
route.register(r'pokemons', pv.PokemonsViewSet, basename='pokemons')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
