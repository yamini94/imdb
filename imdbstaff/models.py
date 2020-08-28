from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ACCESS_LEVEL=(
	('admin','Admin'),
	('user','User'),
)

class UserRole(models.Model):
	name = models.CharField(max_length = 50, db_index=True, unique=True)
	description = models.CharField(max_length = 200, null=True, blank=True)
	permission = models.CharField(max_length=50, default="R")
	access_level = models.CharField(choices=ACCESS_LEVEL, default=ACCESS_LEVEL[0][0], max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('created_date',)

class User(AbstractUser):
	user_role = models.ForeignKey(UserRole, related_name='User_Role',
			null=True, on_delete=models.SET_NULL, blank=True)
	created = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)
	updated = models.DateTimeField(auto_now=True, db_index=True, editable=False)
   
	def __str__(self):
		return self.username
