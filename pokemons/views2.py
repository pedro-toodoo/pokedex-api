import requests 
import asyncio

async def testefun():
    #for i in range(1, 50):
    url = f"https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    requisicao = await requests.get(url)

    lista = requisicao.json()

    print(lista['results'][0]['url'])
    info_pokemon = lista['results'][0]['url']

    #url2 = "lista['results'][0]['url']"
    requisicao2 = requests.get(info_pokemon)

    lista2 = requisicao2.json()
    print(lista2)

asyncio.run(testefun())
