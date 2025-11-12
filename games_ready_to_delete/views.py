from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GameXO
from .utils import check_winner


# SHOW GAMES (ANOTHER HUB YEAHH) :: 

@login_required
def show_games(request):
    """
    Muestra la lista de partidas disponibles y permite crear una nueva.
    """
    games = GameXO.objects.all()

    if request.method == "POST":
        room_name = request.POST.get("room_name")
        if not GameXO.objects.filter(room_name=room_name).exists():
            GameXO.objects.create(owner=request.user, room_name=room_name)
        return redirect("gamesX:allgames")




    return render(request, "games_ready_to_delete/games.html", {"games": games})


# SHOW ACTIVE GAME ::

@login_required
def show_active_game(request, pk):
    """
    Muestra el detalle de una partida (tablero) y permite hacer jugadas.
    """
    game = get_object_or_404(GameXO, pk=pk)
    board = list(game.board)

    if request.method == "POST" and request.user == game.owner and game.state == "active":
        pos = int(request.POST.get("cell"))
        if board[pos] == "_":
            board[pos] = game.active_player
            winner = check_winner(board)
            game.board = "".join(board)

            if winner == "tie":
                game.state = "tie"
            elif winner:
                game.state = "won"
                game.winner = winner
            else:
                game.active_player = "O" if game.active_player == "X" else "X"

            game.save()
            

    # DELETING THE ACTIVE GAME ::
    
    # @WARN => ONLY THE OWNER CAN DELETE IT
    
    if request.GET.get("delete") == "1" and request.user == game.owner:
        game.delete()
        return redirect("gamesX:allgames")

    return render(request, "games_ready_to_delete/game_details.html", {"game": game, "range": range(9), "board_cells": list(game.board)})
