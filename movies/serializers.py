from rest_framework import serializers
from .models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source="genre.name", read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_rating(self, value):
        # value é o valor que veio no JSON para o campo "rating"
        if value < 0 or value > 10:
            # se estiver fora da faixa, levantamos erro de validação (400)
            raise serializers.ValidationError("A nota (rating) deve estar entre 0 e 10.")
        # se estiver ok, retornamos o valor para o DRF continuar o processo
        return value


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
