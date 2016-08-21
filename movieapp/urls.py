from django.conf.urls import url
from . import views
from django.contrib import admin
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     url(r'^movie/search/$', views.movie_search, name='movie_search'),
    


]
