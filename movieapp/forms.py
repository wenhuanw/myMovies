from django import forms
from .models import Movies, SearchMovies

class MovieForm(forms.ModelForm):
   
   class Meta:
      model = SearchMovies
      fields = ('title',)
