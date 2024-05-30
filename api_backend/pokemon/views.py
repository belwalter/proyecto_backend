from django.http import JsonResponse
from django.shortcuts import render
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer

# Create your views here.

def get_all_pokemons():
    pokemons = Pokemon.objects.all().order_by('name')
    pokemons_serializers = PokemonSerializer(pokemons, many=True)
    return pokemons_serializers.data


def pokemons_rest(request):
    pokemons = get_all_pokemons()
    return JsonResponse(pokemons, safe=False)


def index_pok(request):
    pokemons = get_all_pokemons()
    print(pokemons)
    return render(request, 'index_pok.html', {'pokemons': pokemons})