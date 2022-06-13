import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the movie gnre name')

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=150, help_text='Enter the movie name')
    poster_url = models.CharField(max_length=500, help_text='Enter the poster url')
    description = models.TextField(help_text='Enter the movie description')
    short_description = models.CharField(max_length=100, help_text='Enter the movie short description')
    slogan = models.CharField(max_length=50, help_text='Enter the movie slogan')
    film_length = models.IntegerField(help_text='Enter the duration of the movie in minutes')
    age_limit = models.IntegerField(help_text='Enter the movie age limit')
    genre = models.ManyToManyField(Genre, help_text='Select a movie genre')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, related_name='comments_movies')
    comment_text = models.TextField(help_text='Enter the movie comment text')
    comment_date = models.DateTimeField(default=datetime.datetime.now())
    moderation_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-id']


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, related_name='ratings_movies')
    rating = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user}'
