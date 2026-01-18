from django.db import models


class Genre(models.Model):
    # CharField = texto curto com tamanho máximo
    # unique=True = o banco não permite dois gêneros com o mesmo nome
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        # Isso melhora a visualização no Django Admin
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()
    director = models.CharField(max_length=150)
    lead_actor = models.CharField(max_length=150)
    lead_actress = models.CharField(max_length=150)
    is_watched = models.BooleanField(default=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")

    

    def __str__(self):
        return self.title
