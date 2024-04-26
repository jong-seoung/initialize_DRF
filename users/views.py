from django.contrib.auth.hashers import check_password

from core.tokens import TokenResponseSerializer
from users.models import User
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.register_serializers import RegisterSerializer
from .serializers.login_serializers import LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request: Request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                serializer = TokenResponseSerializer(user)
                data = serializer.to_representation(serializer)
                res = Response(
                    data,
                    status=status.HTTP_200_OK,
                )
                return res
            else:
                return Response({'message': 'Password not Match'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)