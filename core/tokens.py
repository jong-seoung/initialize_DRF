from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from core.constants import SystemCodeManager
from core.exceptions import raise_exception

from users.models import User


class TokenResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = TokenObtainPairSerializer.get_token(user)
        self.user = user

    def get_access_token(self):
        return str(self.token.access_token)

    def get_refresh_token(self):
        return str(self.token)

    def to_representation(self, instance):
        nickname = self.user.nickname
        if nickname is None:
            message = "Please set a nickname"
        else:
            message = nickname

        return {
            "message": message,
            "token": {
                "email": self.user.email,
                "access": self.get_access_token(),
                "refresh": self.get_refresh_token(),
            },
        }


def get_user_id(request):
    try:
        auth_header = request.headers.get("Authorization")
        access_token = auth_header.split(" ")[1]
        decoded = AccessToken(access_token)
        user_id = decoded["user_id"]
    except InvalidToken:
        raise_exception(
            code=SystemCodeManager.get_message("auth_code", "TOKEN_INVALID")
        )
    except IndexError:
        raise_exception(
            code=SystemCodeManager.get_message("auth_code", "TOKEN_INVALID")
        )

    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        raise_exception(
            code=SystemCodeManager.get_message("auth_code", "USER_NOT_FOUND")
        )
