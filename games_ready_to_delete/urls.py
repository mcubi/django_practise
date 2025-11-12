from django.urls import path
from . import views

app_name='gamesX'

urlpatterns = [
    path("", views.show_games, name="allgames"),
    path("<int:pk>/", views.show_active_game, name="game_details"),
]
