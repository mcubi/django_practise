from django.db import models
from django.contrib.auth.models import User

# MODELS USED TO CREATE GAMES :: 

class GameXO(models.Model):
    STATE_CHOICES = [
        ('active', 'Active'),
        ('won', 'Won'),
        ('tie', 'Tie'),
    ]
    room_name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=9, default="_________")
    active_player = models.CharField(max_length=1, default="X")
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default="active")
    winner = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.room_name

