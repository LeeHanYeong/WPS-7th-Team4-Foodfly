from rest_framework import permissions, generics
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, SignupSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class ProfileView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        return UserSerializer(request.user).data
