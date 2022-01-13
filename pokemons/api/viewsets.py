from rest_framework import viewsets, generics
from pokemons.api import serializers
from pokemons import models

class PokemonsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PokemonsSerializer
    queryset = models.Pokemons.objects.all() #pegar tds os objetos do model pokemons