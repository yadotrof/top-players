from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows various operations over players.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all().order_by('-highscore')
