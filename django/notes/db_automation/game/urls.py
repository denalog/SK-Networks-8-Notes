from django.urls import path, include
from rest_framework.routers import DefaultRouter

from game.controller.game_controller import GameController

router = DefaultRouter()
router.register(r"game", GameController, basename='game')

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-game',
         GameController.as_view({ 'get': 'requestCreateGame' }),
         name='게임 생성'),
    path('request-check-winner',
         GameController.as_view({ 'get': 'requestCheckWinner' }),
         name='게임 승자 판정'),
]