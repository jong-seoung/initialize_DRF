from rest_framework import viewsets

from boards.serializers import boardsSerializers
from boards.models import Board

class boardsViewsets(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = boardsSerializers