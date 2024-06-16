from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from blogs.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refreshen_token': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
