from rest_framework import serializers
from weiland.backend.models import Art
from weiland.backend.models import Artist
from weiland.backend.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'country']


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ['id', 'title', 'date', 'type', 'description', 'artist']
