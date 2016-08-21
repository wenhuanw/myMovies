from django.conf.urls import url
from . import views
from django.contrib import admin
#from django.contrib.auth import views as auth_views
#import django.contrib.auth.views
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     url(r'^$', views.movie_search, name='movie_search'),
     url(r'^movie/search/(?P<pk>[0-9]+)/$', views.search_detail, name='search_detail'),    
     url(r'^movie/search/add/(?P<pk>[0-9]+)/$', views.movie_add, name='movie_add'),
     url(r'^movie/delete/(?P<pk>[0-9]+)/$', views.movie_delete, name='movie_delete'),
     url(r'^movie/list/$', views.movie_list, name='movie_list'),
     url(r'^movie/detail/(?P<pk>[0-9]+)/$', views.movie_detail, name='movie_detail'),
     url(r'^movie/recommend/list/$', views.recommend_list, name='recommend_list'),
     url(r'^movie/recommend/detail/(?P<pk>[0-9]+)/$', views.recommend_detail, name='recommend_detail'),
     url(r'^movie/recommend/add/(?P<pk>[0-9]+)/$', views.movie_add_rec, name='movie_add_rec'),

     url(r'^api/create/$',views.movie_create_api,name='movie_create_api'),
     url(r'^api/list/$', views.movie_list_api, name='movie_list_api'),
     url(r'^api/id/(?P<pk>[0-9]+)/$', views.movie_id_api, name='movie_id_api'),
   #url(r'^api/list/$',ApiList.as_view(),name='movie_list_api'),
   #url(r'^api/create/$',ApiCreat.as_view(),name='movie_create_api'),
   #url(r'^api/id/(?P<pk>[0-9]+)/$',ApiId.as_view(),name='movie_id_api'),

]
