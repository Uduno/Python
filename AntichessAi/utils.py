from collections import Counter
import time 

# Fonction pour copier récursivement un objet avec ses attributs
def copier_objet(obj):
    if hasattr(obj, '__dict__'):
        copie = type(obj).__new__(type(obj))
        copie.__dict__.update(obj.__dict__)
        return copie
    elif hasattr(obj, '__iter__'):
        return [copier_objet(item) for item in obj]
    else:
        return obj
    
# fonction pour récupérer les movements ayant été joué 3 fois ou + et les supprimer
def antiRepetitiveMove(list_moves):
    repetitive_move = [ move for move in list_moves if list_moves.count(move) >= 2] # on récupère les mouvements qui ont déja été joués 2 fois ou +
    list_moves = [move for move in list_moves if move not in repetitive_move] # on supprime les mouvements répétés 
    return repetitive_move


def miniMax(board, color, depth):
    second_color = "white" if color == "black" else "black"
    pieces_list = board.white_pieces_list if color == "white" else board.black_pieces_list
    best_move = None
    list_moves  = []
    if board.pieceFirstMoves(pieces_list) != []:
        list_moves = board.pieceFirstMoves(pieces_list)
    else:
        list_moves = board.pieceSecondMoves(pieces_list)


    if depth == 0 or board.game_over == True or list_moves == []:
        return board.eval(color)
    
    if depth % 2 == 0:
        maxi = -9999
        for move in list_moves:
            copy_board  = copier_objet(board)
            copy_board.white_pieces_list = copier_objet(board.white_pieces_list)
            copy_board.black_pieces_list = copier_objet(board.black_pieces_list)
            copy_board.makeMove(move, color)
            eval = miniMax(copy_board, second_color, depth - 1)
            copy_board.undoMove(color)
            if eval > maxi:
                maxi = eval
                best_move = move

        return best_move, maxi
    else: # pire coup
        mini = 9999
        for move in list_moves:
            copy_board  = copier_objet(board)
            copy_board.white_pieces_list = copier_objet(board.white_pieces_list)
            copy_board.black_pieces_list = copier_objet(board.black_pieces_list)
            copy_board.makeMove(move, color)
            eval =  miniMax(copy_board, second_color, depth - 1)
            copy_board.undoMove(color)
            if eval < mini:
                mini = eval
                best_move = move
        return best_move, mini
    

def alphaBeta(board, color, depth, alpha, beta):
    second_color = "white" if color == "black" else "black"
    pieces_list = board.white_pieces_list if color == "white" else board.black_pieces_list
    best_move = None
    list_moves  = []
    if board.pieceFirstMoves(pieces_list) != []:
        list_moves = board.pieceFirstMoves(pieces_list)
    else:
        list_moves = board.pieceSecondMoves(pieces_list)

    if depth == 0 or board.game_over == True or list_moves == []:
        return board.eval(color)
    
    if depth % 2 == 0:
        maxi = -9999
        for move in list_moves:
            copy_board  = copier_objet(board)
            copy_board.white_pieces_list = copier_objet(board.white_pieces_list)
            copy_board.black_pieces_list = copier_objet(board.black_pieces_list)
            copy_board.makeMove(move, color)
            eval = alphaBeta(copy_board, second_color, depth - 1, alpha, beta)
            copy_board.undoMove(color)
            if eval > maxi:
                maxi = eval
                best_move = move
            alpha = max(maxi, alpha)
            if alpha <= beta:
                break
        return best_move, maxi
    else: # pire coup
        mini = 9999
        for move in list_moves:
            copy_board  = copier_objet(board)
            copy_board.white_pieces_list = copier_objet(board.white_pieces_list)
            copy_board.black_pieces_list = copier_objet(board.black_pieces_list)
            copy_board.makeMove(move, color)
            eval =  alphaBeta(copy_board, second_color, depth - 1, alpha, beta)
            copy_board.undoMove(color)
            if eval < mini:
                mini = eval
                best_move = move
            beta = min(beta, mini)
            if beta <= alpha:
                break
        return best_move, mini
