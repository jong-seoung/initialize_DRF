from django.contrib.auth.hashers import check_password

from core.tokens import CustomJWTAuthentication
from users.models import User
from rest_framework.request import Request
from rest_framework.views import APIView

from core.exceptions.service_exceptions import *
from core.responses import Response

from .serializers.register_serializers import RegisterSerializer
from .serializers.login_serializers import LoginSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            raise InvalidRequest

        serializer.save()
        return Response(data=serializer.data)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request: Request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                serializer = CustomJWTAuthentication().get_user(user)
                return Response(data=serializer.to_representation(serializer))
            else:
                raise UserPasswordInvalid

        except User.DoesNotExist:
            raise UserNotFound
