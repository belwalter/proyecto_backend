from rest_framework import serializers

from pokemon.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'number', 'type', 'level']