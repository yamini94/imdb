from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Imdb,Genre
from elasticsearch_dsl import Index
from django_elasticsearch_dsl import Document, fields

# @registry.register_document
imdb_index = Index('imdb')

@registry.register_document
@imdb_index.document
class ImdbDocument(Document):

	genre = fields.NestedField(properties={
		'name': fields.TextField()
	})

	class Django:
		model = Imdb
		related_models = [Genre]
		fields = [
			'id',
			'name',
			'popularity',
			'director',
			'imdb_score',
			'created_date',
			'modified_date'
		]
	def get_instances_from_related(self, related_instance):
		return related_instance.imdb_set.all()
	# class Index:
	#     # Index name
	#     name = 'imdb'
	#     settings = {'number_of_shards': 1,
	#                 'number_of_replicas': 0}

	# class Django:
	#     model = Imdb # django model name

	#     # Model fields to display
	#     fields = [
	#         'name',
	#         'popularity',
	#         'director',
	#         'imdb_score',
	#         'genre',
	#         'created_date',
	#         'modified_date'

	#     ]


