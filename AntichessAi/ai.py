import random
import utils
import time

def aiRandom(board, color):
    piece_list = board.white_pieces_list if color == "white" else board.black_pieces_list
    list_moves = []
    if board.pieceFirstMoves(piece_list) != []:
        print("first")
        list_moves = board.pieceFirstMoves(piece_list)
    else:
         print("second")
         list_moves = board.pieceSecondMoves(piece_list)

    move = list_moves[random.randrange(len(list_moves))]
    return move

def aiMiniMax(board, color):
    max_time = 1.5
    start_time = time.time()
    actual_time = 0

    depth = 1
    best_score = -9999
    best_move = []
    
    while actual_time < max_time:
            eval = utils.miniMax(board, color, 1)
            if eval[1] == best_score:
                best_move.append(eval[0])
            if eval[1] > best_score:
                best_score = eval[1]
                best_move.clear()
                best_move.append(eval[0])
            actual_time = time.time() -  start_time
            depth += 1

    print(f'Best_score: {best_score}, Profondeur: {depth}')
    return best_move[random.randrange(len(best_move))] if len(best_move) > 1 else best_move[0]


def aiAlphaBeta(board, color):
    max_time = 1.5
    start_time = time.time()
    actual_time = 0

    depth = 1
    best_score = -9999
    best_move = None
    
    while actual_time < max_time:
            eval = utils.alphaBeta(board, color, 1, -9999, 9999)
            if eval[1] > best_score:
                best_score = eval[1]
                best_move = eval[0]
            actual_time = time.time() -  start_time
            depth += 1
    print(f'Best_score: {best_score}, Profondeur: {depth}')
    return best_move


def aiChoose(choice, board, color):
    match choice:
        case 1:
            return aiRandom(board, color)
        case 2:
            return aiMiniMax(board, color)
        case 3:
            return aiAlphaBeta(board, color)
        case _:
            return aiRandom(board, color)