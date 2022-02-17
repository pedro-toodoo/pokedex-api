from django.urls import path, include
from . import views

from rest_framework import routers

from pokemons.api import viewsets as pv

route = routers.DefaultRouter()
#route.register(r'lista', pv.PokemonsViewSet, basename='lista')

urlpatterns = [    
    path('', include(route.urls)),
    path('pokemons/', views.ListarPokemonsAPIView.as_view(), name='listar-pokemons'),
    path('pesquisa/<str:nome>', views.PesquisarPokemonAPIView.as_view(), name='pesquisar-pokemons')
]