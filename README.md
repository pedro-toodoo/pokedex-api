<h1 align="center"> Pokedex API - Python </h1>

<h4 align="center">   
Marcos contratou a Toodoo para elaborar um projeto de Pokedéx, tal projeto terá aplicativos nativos em Android e IOS e deverão possuir a interface definida pelo time UI/UX disponível no Figma pelo link abaixo:

Cada característica apresentada no Figma deverá vir de uma API criada em Python, que por sua vez consumirá o <a href='https://pokeapi.co/'>PokeAPI</a> (API que retorna as características dos Pokemons). O objetivo dessa API que deverá ser criada é facilitar o acesso entre as aplicações Android e IOS, e a API base PokeAPI.

A nova API desenvolvida em Python, para poder ser consumida pelas aplicações Android e IOS deverá ser hospedada em um domínio e fica livre a escolha dos desenvolvedores, alguns domínios grátis que oferecem suporte para Python são o Heroku e o Google Cloud Platform.
</h4>

## Tópicos 
- [Imagens do REST API](#imagens-do-rest-api) 
- [Informações da API](#informações-da-api-)
- [Passo a passo da implementação](#passo-a-passo-da-implementação-)
- [Instalações](#instalações-)

# Imagens do REST API 
<h4 align='center'>API já em deploy <a href='https://toodoo-pokedex.herokuapp.com/api/v1/pokemons/'>aqui</a>. Endpoint: /api/v1/pokemons lista todos os pokemons</h4>

![image](https://user-images.githubusercontent.com/94690905/149554212-5155ceec-d8b1-4a35-b8b7-61a2f5968630.png)


<h4 align='center'>API já em deploy <a href='https://toodoo-pokedex.herokuapp.com/api/v1/pesquisa/pikachu'>aqui</a>. Endpoint: /api/v1/pesquisa/nome mostra as informações do pokemon informado</h4>
    
![image](https://user-images.githubusercontent.com/94690905/149555388-9b5d7a87-79d6-422d-a150-09e23cfc35e7.png)

<h4 align='center'>O frond end deverá mostrar os cards abaixo (dentre outras telas) com os dados fornecidos pela API:</h4>

![image](https://user-images.githubusercontent.com/94690905/149553517-4e7f9edc-1235-419d-a858-c1911e73c7c9.png)

# Informações da API 📜
- ID
- Nome
- Tipo {nome, cor}
- Peso
- Altura
- Estatísticas {hp, attack, defense, special-attack, special-defense, speed}
- Link_img

# Passo a passo da implementação 🏃
- ### Acessar a PokeAPI
    <h5>Acessando as informações da PokeAPI e consumindo apenas os dados necessários</h5>
- ### Criar Projeto Django
    <h5>Criar um projeto Django, fazer as configurações, instalar pacotes e ambiente virtual</h5>
- ### Fazer deploy em domínio gratuito
    <h5>Deve-se instalar o <a href='https://devcenter.heroku.com/articles/heroku-cli'>Heroku CLI</a> e abrir o bash onde está os arquivos e fazer o login com sua conta heroku e criar um projeto</h5>
    
    ```
    heroku login
    heroku create <nome do dominio>
    ```
    <h5>Fazer os commits para o deploy</h5>   
    
    ```
    git add .
    git commit -m "deploy"
    git push heroku master
    ```
    
- ### Implementar Django REST Framework
    <h5>Utilizar padrão REST para e conseguir acessar os dados em JSON pelo navegador</h5>

# Instalações 🔧

- 1º: instalar o Django:
```
pip install django 
```
- 2º: instalar o REST framework:
```
pip install djangorestframework 
```
- 3º: instalar o Requests:
```
pip install requests 
```
- 4º: instalar o gunicorn:
```
pip install gunicorn 
```
- 1º: instalar o Django-heroku:
```
pip install django-heroku 
```
