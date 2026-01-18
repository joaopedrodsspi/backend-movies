from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Genre
from .serializers import GenreSerializer

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # POST /movies/
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "message": "Erro de validação",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        movie = serializer.save()

        return Response(
            {
                "message": "Filme cadastrado com sucesso",
                "data": self.get_serializer(movie).data,
            },
            status=status.HTTP_201_CREATED,
        )

    # GET /movies/{id}/
    def retrieve(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = self.get_serializer(movie)

        return Response(
            {
                "message": "Detalhes do filme",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # PUT /movies/{id}/
    # PATCH /movies/{id}/
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        movie = self.get_object()

        serializer = self.get_serializer(
            movie,
            data=request.data,
            partial=partial,
        )

        if not serializer.is_valid():
            return Response(
                {
                    "message": "Erro de validação",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()

        return Response(
            {
                "message": "Filme atualizado com sucesso",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # DELETE /movies/{id}/
    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.delete()

        return Response(
            {
                "message": "Filme removido com sucesso",
            },
            status=status.HTTP_204_NO_CONTENT,
        )
        
    @action(detail=False, methods=["get"], url_path="rating-maior-igual-7")
    def rating_maior_igual_7(self, request):
        movies = Movie.objects.filter(rating__gte=7)
        serializer = self.get_serializer(movies, many=True)

        return Response(
            {
                "message": "Filmes com nota maior ou igual a 7",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )




class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer