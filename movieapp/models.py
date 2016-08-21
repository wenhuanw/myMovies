from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_id = models.IntegerField(default=0, null=True, blank=True)
    title = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    rate = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    genre_id = models.IntegerField(default=0, blank=True, null=True)
    poster_path = models.CharField(max_length=100, blank=True)
    overview = models.TextField(max_length=5000, blank=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title



class SearchMovies(models.Model):
    movie_id = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    genre_id = models.IntegerField(default=0, null=True)
    poster_path = models.CharField(max_length=100, blank=True)
    overview = models.TextField(max_length=5000, blank=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class RecommendMovies(models.Model):
    movie_id = models.IntegerField(default=0, null=True, blank=True)
    title = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    rate = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    genre_id = models.IntegerField(default=0, blank=True, null=True)
    poster_path = models.CharField(max_length=100, blank=True)
    overview = models.TextField(max_length=5000, blank=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title
