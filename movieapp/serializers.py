
from rest_framework import serializers
from movieapp.models import Movies, RecommendMovies, SearchMovies 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('movie_id', 'title', 'date', 'rate', 'genre_id', 'poster_path', 'overview')
    movie_id = serializers.IntegerField(default=0)
    title = serializers.CharField(max_length=50)
    date = serializers.CharField(max_length=50)
    rate = serializers.DecimalField(max_digits=5,decimal_places=2)
    genre_id = serializers.IntegerField(default=0)
    poster_path = serializers.CharField(max_length=100)
    overview = serializers.CharField(max_length=5000)

def create(self, validated_data):
       """ 
       Create and return a new `Users` instance, given the validated data.      
       """
       return Movies.objects.create(**validated_data)


def update(self, instance, validated_data):
      instance.movie_id = validated_data.get('movie_id', instance.movie_id)
      instance.title = validated_data.get('title', instance.title)
      instance.date = validated_data.get('date', instance.date)
      instance.rate = validated_data.get('rate', instance.rate)
      instance.genre_id = validated_data.get('genre_id', instance.genre_id)
      instance.poster_path = validated_data.get('poster_path', instance.poster_path)
      instance.overview = validated_data.get('overview', instance.overview)
      instance.save()
      return instance


class MovieSerializer_s(serializers.ModelSerializer):
    class Meta:
        model = SearchMovies
        fields = ('movie_id', 'title', 'date', 'rate', 'genre_id', 'poster_path', 'overview')
    movie_id = serializers.IntegerField(default=0)
    title = serializers.CharField(max_length=50)
    date = serializers.CharField(max_length=50)
    rate = serializers.DecimalField(max_digits=5,decimal_places=2)
    genre_id = serializers.IntegerField(default=0)
    poster_path = serializers.CharField(max_length=100)
    overview = serializers.CharField(max_length=5000)



def create(self, validated_data):
       """ 
       Create and return a new `Users` instance, given the validated data.      
       """
       return Movies.objects.create(**validated_data)


def update(self, instance, validated_data):
      instance.movie_id = validated_data.get('movie_id', instance.movie_id)
      instance.title = validated_data.get('title', instance.title)
      instance.date = validated_data.get('date', instance.date)
      instance.rate = validated_data.get('rate', instance.rate)
      instance.genre_id = validated_data.get('genre_id', instance.genre_id)
      instance.poster_path = validated_data.get('poster_path', instance.poster_path)
      instance.overview = validated_data.get('overview', instance.overview)
      instance.save()
      return instance




class MovieSerializer_r(serializers.ModelSerializer):
    class Meta:
        model = RecommendMovies
        fields = ('movie_id', 'title', 'date', 'rate', 'genre_id', 'poster_path', 'overview')
    movie_id = serializers.IntegerField(default=0)
    title = serializers.CharField(max_length=50)
    date = serializers.CharField(max_length=50)
    rate = serializers.DecimalField(max_digits=5,decimal_places=2)
    genre_id = serializers.IntegerField(default=0)
    poster_path = serializers.CharField(max_length=100)
    overview = serializers.CharField(max_length=5000)



def create(self, validated_data):
       """ 
       Create and return a new `Users` instance, given the validated data.      
       """
       return Movies.objects.create(**validated_data)


def update(self, instance, validated_data):
      instance.movie_id = validated_data.get('movie_id', instance.movie_id)
      instance.title = validated_data.get('title', instance.title)
      instance.date = validated_data.get('date', instance.date)
      instance.rate = validated_data.get('rate', instance.rate)
      instance.genre_id = validated_data.get('genre_id', instance.genre_id)
      instance.poster_path = validated_data.get('poster_path', instance.poster_path)
      instance.overview = validated_data.get('overview', instance.overview)
      instance.save()
      return instance
