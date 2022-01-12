from django.urls import path, include
from . import views

from rest_framework import routers, urlpatterns

from pokemons.api import viewsets as pv

route = routers.DefaultRouter()
route.register(r'lista', pv.PokemonsViewSet, basename='pokemons')

urlpatterns = [    
    path('', include(route.urls)),
    path('json/', views.pokemons)
    #path('lista/', views.PokedexAPIView.as_view(), name='lista')
]