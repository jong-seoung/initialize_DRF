from rest_framework import serializers

from api.models.boards.models import Board


class boardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
