from django.db import models
from uuid import uuid4

class Pokemons(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nome = models.CharField(max_length=30)
