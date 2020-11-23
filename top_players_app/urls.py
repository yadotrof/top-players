from django.urls import path
from .views import PlayerViewSet

player_all = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

player_concrete = PlayerViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
})

urlpatterns = [
     path('players/', player_all, name='player-all'),
     path('players/<int:pk>/', player_concrete, name='player-concrete'),
]
