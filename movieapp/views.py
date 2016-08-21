from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Movies, SearchMovies
from .forms import MovieForm
from django.conf import settings
from .myservice import search, searchById
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
import pdb
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from movieapp.serializers import MovieSerializer
from ratelimit.decorators import ratelimit

# Create your views here.
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='login/')
def movie_search(request):
   if request.method == "POST":
      SearchMovies.objects.all().delete()
      form = MovieForm(request.POST)
      if form.is_valid():
         movie = form.save()
        # pdb.set_trace()
         movie_list = search(movie.title)
        # print (len(movie_list))
         SearchMovies.objects.all().delete()
         i = 0
         for m in movie_list:
            if (i >= 15):
               break
            if (m['vote_average'] < 5):
               continue
            movie = SearchMovies.objects.create(movie_id = m['id'])
            movie.title = m['title']
            movie.date = m['release_date']
            movie.rate = m['vote_average']
            if (len(m['genre_ids']) > 0):
               movie.genre_id = m['genre_ids'][0]
            if (m['poster_path'] is not None):
               movie.poster_path =  "https://image.tmdb.org/t/p/original" + m['poster_path']
            movie.overview = m['overview']
            movie.save()
            i = i + 1
         search_list = SearchMovies.objects.all()
         return render(request,'movieapp/search_list.html',{'form':form, 'search_list':search_list})
   else:
      form = MovieForm()
      return render(request, 'movieapp/movie_form.html',{'form':form})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='login/')
def search_detail(request, pk):
    movie = get_object_or_404(SearchMovies, pk=pk)
    return render(request, 'movieapp/search_detail.html', {'movie': movie})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='login/')
def movie_add(request, pk):
    search_movie = get_object_or_404(SearchMovies, pk=pk)
    movie = Movies.objects.create(movie_id = search_movie.movie_id, title = search_movie.title, date = search_movie.date, rate = search_movie.rate, genre_id = search_movie.genre_id, poster_path = search_movie.poster_path, overview = search_movie.overview)
    search_list = SearchMovies.objects.all()
    movie.save()
    return render(request, 'movieapp/search_list.html',{'search_list':search_list})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='login/')
def movie_list(request):
    movie_list = Movies.objects.all()
    return render(request, 'movieapp/movie_list.html', {'movie_list':movie_list})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='login/')
def movie_detail(request, pk):
   movie = get_object_or_404(Movies, pk=pk)
   return render(request, 'movieapp/movie_detail.html', {'movie': movie}) 

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='login/')
def movie_delete(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if (movie is not None):
       movie.delete()
    return movie_list(request)  



@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET'])
def movie_list_api(request):
    if request.method == "GET":
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data)

    return Response(status=status.HTTP_401_UNAUTHORIZED)


@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['POST'])
def movie_create_api(request):
    if request.method == "POST":
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET','DELETE'])
def movie_id_api(request, pk, format=None):
    try:
        movie= Movies.objects.get(movie_id = pk)
    except movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED)



