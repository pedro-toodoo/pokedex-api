from base64 import encode
from rest_framework import serializers
#from pokemons import models

class PokemonsSerializer(serializers.Serializer):
    ID = serializers.IntegerField()
    Nome = serializers.CharField(max_length=255)
    Tipo = serializers.JSONField()
    #tipo_cor = serializers.JSONField()
    Peso = serializers.IntegerField()
    Altura = serializers.IntegerField()
    Habilidades = serializers.JSONField()
    Estatisticas = serializers.JSONField()
    Link_img = serializers.CharField(max_length=255)