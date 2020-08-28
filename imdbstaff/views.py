from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from imdb.utility import get_object
# Create your views here.

class CreateEditUserApiView(APIView):
	'''
	This view is used to save and get data of website visitors
	'''
	serializer_class = UserSerializer
	permission_classes = [AllowAny]

	def post(self, request, pk=None):
		if pk:
			object_data = get_object(pk, "imdbstaff", "User")
			user_serializer = self.serializer_class(object_data, data=request.data)
			msg="User updated succefully"
		else:
			user_serializer = self.serializer_class(data=request.POST)
			msg="User created succefully"
		if user_serializer.is_valid():
			user_data = user_serializer.save()
			user_data.set_password(request.POST["password"])
			user_data.save()
			if not pk:
				Token.objects.get_or_create(user=user_data)
			print("user data saved succefully")
			return JsonResponse({"status":"success","msg":msg}, status=200)
		return JsonResponse({"result":user_serializer.errors,"status":"error"}, status=500)


