from django.urls import path
from pokemon import views

urlpatterns = [
    path('index_pokemon', views.index_pok, name='index_pokemon'),
    path('pokemons_rest/', views.pokemons_rest, name='pokemons_rest'),
]