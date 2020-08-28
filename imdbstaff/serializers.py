from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','password','user_role')
	def validate(self, data):
		if 'user_role' not in data:
			print("miniiiiii")
			raise serializers.ValidationError({"user_role": ["This field is required. with value admin use 1 and for user use 2"]})
		return data