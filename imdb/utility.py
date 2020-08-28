from django.shortcuts import get_object_or_404
from django.apps import apps

def get_object(pk, app_name, model_name):
	"""
	This method is used to get object from particular model 
	"""
	model = apps.get_model(app_label=app_name, model_name=model_name)
	return get_object_or_404(model, pk=pk)