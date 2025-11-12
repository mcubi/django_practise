# FILE DEDICATED TO GAME LOGIC :: 


# @ GameXO ( Tic tac toe )

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] != "_" and board[a] == board[b] == board[c]:
            return board[a]
    if "_" not in board:
        return "tie"
    return None

# @ any
