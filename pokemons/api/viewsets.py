from rest_framework import viewsets
from rest_framework.serializers import SerializerMetaclass
from pokemons.api import serializers
from pokemons import models

class PokemonsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PokemonsSerializer
    queryset = models.Pokemons.objects.all() #pegar tds os objetos do model pokemons