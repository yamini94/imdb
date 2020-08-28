from django.db import models

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=30, unique=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name
		
class Imdb(models.Model):
	name = models.CharField(max_length = 200, db_index=True, unique=True)
	popularity = models.FloatField(default=0.0)
	director = models.CharField(max_length = 200, null=True, blank=True)
	imdb_score = models.FloatField(default=0.0)
	genre = models.ManyToManyField(Genre)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('created_date',)
