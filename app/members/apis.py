from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, SignupSerializer, EmailAuthTokenSerializer

__all__ = (
    'SignupView',
    'AuthTokenView',
    'ProfileView',
)


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class AuthTokenView(APIView):
    def post(self, request):
        serializer = EmailAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        data = {
            'user': UserSerializer(user).data,
            'token': user.token,
        }
        return Response(data)


class ProfileView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        return Response(UserSerializer(request.user).data)
