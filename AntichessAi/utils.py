from collections import Counter
import time 
import random

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
            if eval == 999:
                return move, eval
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
            if eval == 999:
                return move, eval
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
# creer un noeud de l'arbre mtct Chaque nœud représente un état du jeu.
class MCTSNode:
    def __init__(self, board, move=None, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
#Sélectionne un nœud à explorer en utilisant l'algorithme UCT. Parcourt les nœuds jusqu'à trouver un nœud non visité ou un nœud sans enfants.
def select(node,color):
    while node.children:
        node = max(node.children, key=lambda child: uct(child, node.visits))
    if node.visits == 0:
        return node
    else:
        return expand(node,color)
#Étend le nœud en générant tous ses enfants possibles. Crée de nouveaux nœuds pour chaque mouvement légal.
def expand(node, color):
    possible_moves = node.board.get_legal_moves(color)

    if not possible_moves:
        return None  # Aucune possibilité de mouvement trouvée

    for move in possible_moves:
        new_board = copier_objet(node.board)
        new_board.white_pieces_list = copier_objet(node.board.white_pieces_list)
        new_board.black_pieces_list = copier_objet(node.board.black_pieces_list)
        new_board.makeMove(move, color)
        child_node = MCTSNode(new_board, move, parent=node)
        node.children.append(child_node)
    return random.choice(node.children) if node.children else None
# Simule une partie complète de manière aléatoire à partir de ce nœud. Continue jusqu'à la fin de la partie et retourne le résultat.
def simulate(node, color):
    board_copy = copier_objet(node.board)
    board_copy.white_pieces_list = copier_objet(node.board.white_pieces_list)
    board_copy.black_pieces_list = copier_objet(node.board.black_pieces_list)
    current_color = color
    while not board_copy.game_over:
        possible_moves = board_copy.get_legal_moves(current_color)
        if not possible_moves:
            break
        move = random.choice(possible_moves)
        board_copy.makeMove(move, current_color)
        current_color = "white" if current_color == "black" else "black"
    return 1 if board_copy.get_winner() == color else 0
#Propager les résultats d'une simulation jusqu'à la racine de l'arbre.  Met à jour les statistiques de chaque nœud traversé (visites et victoires).
def backpropagate(node, result):
    while node is not None:
        node.visits += 1
        node.wins += result
        node = node.parent
#    Calculer la valeur UCT pour un nœud.
def uct(node, parent_visits):
    C = 1.4  # Exploration parameter
    if node.visits == 0:
        return float('inf')
    return node.wins / node.visits + C * (2 * (parent_visits ** 0.5) / node.visits)
