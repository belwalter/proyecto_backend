from django.urls import path
from pokemon import views

urlpatterns = [
    path('pokemons_rest/', views.pokemons_rest, name='pokemons_rest'),
]