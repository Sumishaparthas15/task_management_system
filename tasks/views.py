from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
class UserLoginView(TokenObtainPairView):
    pass  