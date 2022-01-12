from django.shortcuts import render
import requests
from django.http import JsonResponse

def pokemons(request):
    #listas auxiliares
    tipo = [] #aux tipo
    habil = [] #aux habilidade
    stat = [] #aux statisticas
    lista_hab = [] 
    lista_tipo = []
    lista_aux = []
    lista_stat = []

    #dicionários 
    dicio_stat = {}
    dicio_todos = {}
    dicio_aux = {}

    for i in range(1, 101):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        requisicao = requests.get(url)

        try:
            lista = requisicao.json()
        except ValueError:
            print("ERRO TIPO")


        dicio = {
            'ID': lista['id'],
            'Nome': lista['name'],
            'Tipo': lista_tipo,
            'Peso': lista['weight'],
            'Altura': lista['height'],
            'Habilidades': lista_hab,
            'Estatisticas': dicio_stat,
            'Link_img': lista['sprites']['other']['official-artwork']['front_default']
        }

        for a in lista['abilities']:
            #dic_abi[i['ability']['name']] = i['ability']['url']
            habil.append(a['ability']['name'])
        dicio['Habilidades'] = habil[:]
        lista_hab.append(dicio.copy())


        for s in lista['stats']:
            stat.append({s['stat']['name']: s['base_stat']}) 
        dicio['Estatisticas'] = stat[:] 
        lista_stat.append(dicio.copy())
        

        for t in lista['types']:
            #dic_type[i['type']['name']] = i['type']['url']
            tipo.append(t['type']['name'])
        dicio['Tipo'] = tipo[:]
        lista_tipo.append(dicio.copy())

        dicio_aux = dicio.copy()
        lista_aux.append(dicio_aux)

        dicio_todos['pokemons'] = lista_aux

        habil.clear()
        tipo.clear()
        stat.clear()
        dicio.clear()

    return JsonResponse(dicio_todos)

    #return render(request, "index.html", contexto)
