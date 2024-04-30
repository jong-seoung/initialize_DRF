from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

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
    auth_header = request.headers.get("Authorization")
    access_tokne = auth_header.split(" ")[1]
    decoded = AccessToken(access_tokne)
    user_id = decoded["user_id"]
    user_instance = User.objects.get(id=user_id)
    return user_instance
