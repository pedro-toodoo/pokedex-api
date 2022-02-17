import imp
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pokemons.api import viewsets as pv
from pokemons import urls

route = routers.DefaultRouter()
#route.register(r'lista', pv.PokemonsViewSet, basename='lista')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/v1/', include('pokemons.urls'))
]
