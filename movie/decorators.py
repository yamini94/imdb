from django.http import JsonResponse, HttpResponseRedirect
from django.urls import resolve
from django.urls import reverse
from rest_framework.response import Response
from django.conf import settings
from .models import *
import pickle

def user_validation(function):
	"""
	This validation is used to do validation of
	user is already exist or not with same detail
	"""
	def wrap(request, *args, **kwargs):
		if request.method not in request.user.user_role.permission:
			msg = "This operation is not allowed"
			return JsonResponse({"result":{"permission":["This operation is not allowed"]},"msg":msg}, status=401)
		return function(request, *args, **kwargs)
	return wrap