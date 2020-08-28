from rest_framework import serializers

from .models import *
from.documents import ImdbDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Imdb
		fields = ('name','popularity','director','imdb_score')

class MovieListSerializer(serializers.ModelSerializer):
	genre = serializers.SerializerMethodField()
	class Meta:
		model = Imdb
		fields = ('id','name','popularity','director','imdb_score','genre','created_date','modified_date')

	def get_genre(self, obj):
		if obj.genre.all().exists():
			return list(obj.genre.all().values_list("name",flat=True))
		else:
			return []

# class ImdbDocumentSerializer(DocumentSerializer):
#     """Serializer for the Book document."""

#     class Meta(object):
#         """Meta options."""

#         # Specify the correspondent document class
#         document = ImdbDocument

#         # List the serializer fields. Note, that the order of the fields
#         # is preserved in the ViewSet.
#         fields = (
#             'id',
#             'name',
#             'popularity',
#             'director',
#             'imdb_score',
#             'genre',
#             'created_date',
#             'modified_date'
#         )