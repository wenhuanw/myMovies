from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5,decimal_places=2)
    genre_id = models.IntegerField(default=0)
    poster_path = models.CharField(max_length=100)
    overview = models.TextField(max_length=5000)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title



class SearchMovies(models.Model):
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    genre_id = models.IntegerField(default=0)
    poster_path = models.CharField(max_length=100)
    overview = models.TextField(max_length=5000)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title

