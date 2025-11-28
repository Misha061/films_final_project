from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    photoname = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.title}"

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})

class FilmComment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment}"
    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})

class FilmScore(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.score}"


    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})