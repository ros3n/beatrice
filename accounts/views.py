from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from rest_framework.views import APIView
from accounts.serializers import UserSerializer


class RegisterUserView(APIView):
    """View to register a new user"""
    def post(self, request):
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            user = User.objects.create_user(**request.DATA)
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response(UserSerializer(instance=request.user).data)
