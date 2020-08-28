from django.urls import path
from . import views
urlpatterns = [
 	path('imdbstaff/movies/', views.MovieApiView.as_view(), name="movies"),
    path('imdbstaff/movies/create/', views.CreateEditDeleteMovieApiView.as_view(), name="movies_create"),
    path('imdbstaff/movies/<int:pk>/', views.CreateEditDeleteMovieApiView.as_view(), name="movies_edit"),
    path('imdbstaff/search/', views.SearchMovieApiView.as_view(), name="movies_search"),
]