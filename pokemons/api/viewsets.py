from rest_framework import viewsets
from pokemons.api import serializers
from pokemons import models
from pokemons.views import ListarPokemonsAPIView, pokemons

class PokemonsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PokemonsSerializer
    queryset = models.Pokemons.objects.all() #pegar tds os objetos do model pokemons