from django.shortcuts import render
from django.apps import apps
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from .decorators import (user_validation)
from .serializers import MovieSerializer,MovieListSerializer
from .models import Imdb, Genre
from .documents import ImdbDocument
from imdb.utility import get_object
# Create your views here.

@method_decorator(user_validation, name='get')
class MovieApiView(generics.ListAPIView):
	"""
	List all tutorial videos.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Imdb.objects.all()
	serializer_class = MovieListSerializer

@method_decorator(user_validation, name='post')
@method_decorator(user_validation, name='delete')
class CreateEditDeleteMovieApiView(APIView):
	'''
	This view is used to show,create,edit and delete movie
	'''
	permission_classes = [IsAuthenticated]
	serializer_class = MovieSerializer

	def post(self, request,  pk=""):
		movies = request.data
		if pk:
			object_data = get_object(pk, "movie", "Imdb")
			movie_serializer = self.serializer_class(object_data, data=movies)
			msg="Movie updated succefully"
		else:
			movie_serializer = self.serializer_class(data=movies)
			msg="Movies created succefully"
		if "99popularity" in movies:
			movies['popularity'] = movies['99popularity']
		if movie_serializer.is_valid():
			movie_instance = movie_serializer.save()
			movie_instance.genre.clear()
			if 'genre' in movies: 
				for gnr in movies['genre']:
					gnr_obj, created = Genre.objects.get_or_create(name=gnr)
					movie_instance.genre.add(gnr_obj.id)
			return JsonResponse({"msg":msg}, status=200)
		return JsonResponse({"result":movie_serializer.errors,"status":"error"}, status=500)
	
	def delete(self, request, pk=""):
		if pk:
			imdb_data = Imdb.objects.filter(pk=pk)
			if imdb_data.exists():
				imdb_data.delete()
				return JsonResponse({"msg":"Movie with id %s deleter succefully"%pk}, status=200)				
			else:
				return JsonResponse({"msg":"Movie with this id does not exist","status":"error"}, status=500)				

		return JsonResponse({"msg":"pk is required","status":"error"}, status=500)

class SearchMovieApiView(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = MovieListSerializer
	model = Imdb
	paginate_by = 100
	def get_queryset(self):
		search_word = self.request.query_params.get('search', None)
		if search_word:
			queryset = ImdbDocument.search().filter("match", name=search_word).to_queryset()
		else:
			queryset = ImdbDocument.search().to_queryset()
		return queryset.order_by('-created_date')