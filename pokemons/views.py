from django import views
from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from pokemons.api import serializers
import asyncio
import aiohttp
import ssl

def pokemons():
    #listas auxiliares
    tipo = [] #aux tipo
    habil = [] #aux habilidade
    stat = [] #aux statisticas
    cor = [] #aux cor do tipo
    lista_aux = []

    #dicionários 
    dicio_todos = {}
    dicio_aux = {}
    dicio_tipo_cor = {}        
    dicio_cor = {
            'rock': '#B69E31',
            'ghost': '#70559B',
            'steel': '#B7B9D0',
            'water': '#6493EB',
            'grass': '#74CB48',
            'psychic': '#FB5584',
            'ice': '#9AD6DF',
            'dark': '#75754C',
            'fairy': '#E69EAC',
            'normal': '#AAA67F',
            'fighting': '#C12239',
            'flying': '#A891EC',
            'poison': '#A43E9E',
            'ground': '#DEC16B',
            'bug': '#A7B723',
            'fire': '#F57D31',
            'electric': '#F9CF30',
            'dragon': '#7037FF'
    }

    for i in range(1, 10):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        requisicao = requests.get(url)

        try:
            lista = requisicao.json()
        except ValueError:
            print("Os dados não estão em formato JSON")
    
        dicio = {
            'ID': lista['id'],
            'Nome': lista['name'],
            'Tipo': cor, 
            'Peso': lista['weight'],
            'Altura': lista['height'],
            'Habilidades': habil,
            'Estatisticas': stat,
            'Link_img': lista['sprites']['other']['official-artwork']['front_default']
        }

        for a in lista['abilities']:
            habil.append(a['ability']['name'])
        dicio['Habilidades'] = habil[:]


        for s in lista['stats']:
            stat.append({s['stat']['name']: s['base_stat']}) 
        dicio['Estatisticas'] = stat[:] 
        
        for t in lista['types']:
            #tipo.append(t['type']['name'])
            for i, v in enumerate(dicio_cor):
                if t['type']['name'] == v:
                    dicio_tipo_cor['nome'] = v
                    dicio_tipo_cor['cor'] = dicio_cor[v]
                    cor.append(dicio_tipo_cor.copy())
        dicio['Tipo'] = cor[:]


        dicio_aux = dicio.copy()
        lista_aux.append(dicio_aux)

        dicio_todos['pokemons'] = lista_aux

        habil.clear()
        tipo.clear()
        stat.clear()
        dicio_tipo_cor.clear()
        cor.clear()
        dicio.clear() 

    return dicio_todos
    print(lista)

class ListarPokemonsAPIView(views.APIView):
    """
    API Listando pokemons - Blastoff
    """
    def get(self, request):
        requisicao = pokemons()

        valor = serializers.PokemonsSerializer(requisicao['pokemons'], many=True).data

        return Response(valor)

class PesquisarPokemonAPIView(views.APIView):
    """
    API pesquisando pokemons - Blastoff
    """
    def get(self, request, nome):        
        requisicao = pokemons()
        valor = ""
        for i, v in enumerate(requisicao['pokemons']):
            if nome == v['Nome']:
                valor = requisicao['pokemons'][i]
                result = serializers.PokemonsSerializer(valor).data
                break
        
        return Response(result)