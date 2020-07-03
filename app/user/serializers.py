from django.contrib.auth import get_user_model ,authentication
from rest_framework import serializers
from django.utlis.translation import ugettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for users object  """

    class Meta:
        model = get_user_model()
        fields = ('email','password','name')
        extra_kwargs = {'password': {'write_only':True, 'min_length':5}}

    def create(self,validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model()..objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for user authentication model """
    email = serializers.CharField()
    password = serializers.CharField(
        style =('input_type': 'password')
        trim_whitespace=False
    )
    




