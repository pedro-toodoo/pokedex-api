from rest_framework import serializers
from pokemons import models

class PokemonsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Pokemons
        fields = '__all__'