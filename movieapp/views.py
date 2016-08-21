from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Movies, SearchMovies
from .forms import MovieForm
from django.conf import settings
from .myservice import search, searchById

# Create your views here.
def movie_search(request):
   if request.method == "POST":
      SearchMovies.objects.all().delete()
      form = MovieForm(request.POST)
      if form.is_valid():
         movie = form.save()
         movie_list = search(movie.title)
         SearchMovies.objects.all().delete()
         i = 0
         for m in movie_list:
            if (i >= 10):
               break
            movie = SearchMovies.objects.create(movie_id = m['id'])
            movie.title = m['title']
            movie.date = m['release_date']
            movie.rate = m['vote_average']
            movie.genre_id = m['genre_ids'][0]
            movie.poster_path = m['poster_path']
            movie.overview = m['overview']
            movie.save()
            i = i + 1
         search_list = SearchMovies.objects.all()
         return render(request,'movieapp/search_list.html',{'form':form, 'search_list':search_list})
   else:
      form = MovieForm()
      return render(request, 'movieapp/url_form.html',{'form':form})
