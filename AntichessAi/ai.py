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

class MCTSNode:
    def __init__(self, board, move=None, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

def aiMCTS(board, color):
    max_time = 1.5
    start_time = time.time()
    root = MCTSNode(board)

    while time.time() - start_time < max_time:
        leaf = select(root,color)
        simulation_result = simulate(leaf, color)
        backpropagate(leaf, simulation_result)
    
    if not root.children:
        raise ValueError("No valid moves found")
    
    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.move


def select(node,color):
    while node.children:
        node = max(node.children, key=uct)
    if node.visits == 0:
        return node
    else:
        return expand(node,color)

def expand(node,color):
    if node.parent is None:
        possible_moves = node.board.get_legal_moves(color)  # Obtenir les mouvements possibles pour la couleur actuelle
    else:
        possible_moves = node.board.get_legal_moves(node.parent.move[0])  # Utiliser la couleur du joueur parent

    if not possible_moves:
        print("No possible moves found during expand")
    for move in possible_moves:
        new_board = node.board.copy()
        new_board.makeMove(move, node.parent.move[0] if node.parent else color)  # Utiliser la couleur du joueur parent ou la couleur actuelle si c'est la racine
        child_node = MCTSNode(new_board, move, parent=node)  # Assigner le mouvement au nœud enfant
        node.children.append(child_node)
    return random.choice(node.children) if node.children else node

def simulate(node, color):
    board_copy = node.board.copy()
    current_color = color
    while not board_copy.game_over:
        possible_moves = board_copy.get_legal_moves(current_color)
        if not possible_moves:
            break
        move = random.choice(possible_moves)
        board_copy.makeMove(move, current_color)
        current_color = "white" if current_color == "black" else "black"
    return 1 if board_copy.get_winner() == color else 0



def backpropagate(node, result):
    while node is not None:
        node.visits += 1
        node.wins += result
        node = node.parent


def uct(node):
    C = 1.4  # Exploration parameter
    if node.visits == 0:
        return float('inf')
    return node.wins / node.visits + C * (2 * (node.parent.visits ** 0.5) / node.visits)

def aiChoose(choice, board, color):
    match choice:
        case 1:
            return aiRandom(board, color)
        case 2:
            return aiMiniMax(board, color)
        case 3:
            return aiAlphaBeta(board, color)
        case 4:
            return aiMCTS(board, color)
        case _:
            return aiRandom(board, color)