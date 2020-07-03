from user.serializers import UserSerializer
from rest_framework import generic 

class CreateUserView(generic.CreateAPIView):
    serializer_class = UserSerializer
    

