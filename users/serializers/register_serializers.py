from rest_framework import serializers

from core.exceptions.service_exceptions import *

from users.models import User


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(
        max_length=255, required=True, write_only=True, label="[Input]이메일"
    )
    password = serializers.CharField(
        max_length=128, required=True, write_only=True, label="[Input]패스워드"
    )

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise UserAlreadyExists
        return data

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(email=email, password=password)

        return user
