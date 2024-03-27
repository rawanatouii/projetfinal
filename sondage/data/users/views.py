from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
