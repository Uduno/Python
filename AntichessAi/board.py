# Plateau de jeu
import piece as Piece
import utils

class Board():
    def __init__(self, size) -> None:
        self.size = size
        self.board = [["__"] * size for x in range(size)]  # tableau 2d rempli de string vide
        self.white_pieces_list = []
        self.black_pieces_list = []
        self.white_pieces_list_history = []
        self.black_pieces_list_history = []
        self.moves_history = []
        self.game_over = None
        self.initBoard()
        self.initPiece()
    
    def showBoard(self):
        for row in range(self.size):
            for col in range(self.size):
                print(f'[{self.board[row][self.size - 1 - col]}]', end='')
            print("")
        print("")

    def initPiece(self):
        pass

    def initBoard(self):
        pass

    def updateBoard(self, color): # on met à jour le plateau
        list_piece1 = self.white_pieces_list if color == "white" else self.black_pieces_list
        list_piece2 = self.black_pieces_list if color == "white" else self.white_pieces_list
        self.board = [["__"] * self.size for x in range(self.size)] 
        for piece in list_piece2:
            self.board[piece.pos_x][piece.pos_y] = piece.name
        for piece in list_piece1:
            self.board[piece.pos_x][piece.pos_y] = piece.name 
    
    def verifyBoard(self): # on vérifie la présence réelle des pièces
        for piece in self.white_pieces_list:
            if self.board[piece.pos_x][piece.pos_y] != piece.name:
                self.white_pieces_list.remove(piece)
        for piece in self.black_pieces_list:
            if self.board[piece.pos_x][piece.pos_y] != piece.name:
                self.black_pieces_list.remove(piece)
    
    def updatePion(self):
        for piece in self.white_pieces_list:
            if piece.name == "BP" and piece.pos_x == 0:
                new_piece = Piece.Roi("BK",piece.pos_x, piece.pos_y, piece.id, self)
                self.white_pieces_list.remove(piece)
                self.white_pieces_list.append(new_piece)
        for piece in self.black_pieces_list:
            if piece.name == "NP" and piece.pos_x == self.size - 1:
                new_piece = Piece.Roi("NK",piece.pos_x, piece.pos_y, piece.id, self)
                self.black_pieces_list.remove(piece)
                self.black_pieces_list.append(new_piece)

    def pieceFirstMoves(self, piece_list): # mouvements avec capture
        first_moves_list = []
        # print(piece_list[0].moves())
        first_moves = [piece.moves()[0] for piece in piece_list]
        for first_move in first_moves:
            for moves in first_move:
                
                if moves != []:
                    first_moves_list.append(moves)
                    
        return first_moves_list

    def pieceSecondMoves(self, piece_list): # mouvements sans capture
        second_moves_list = []
        second_moves = [piece.moves()[1] for piece in piece_list]
        repetitive_moves= utils.antiRepetitiveMove(self.moves_history)
        for second_move in second_moves:
            for moves in second_move:
                if moves != [] and moves not in repetitive_moves:
                    second_moves_list.append(moves)
        return second_moves_list

    def makeMove(self, move, color):
        # on sauvegarde l'état des pièces avant le coup
        self.white_pieces_list_history = utils.copier_objet(self.white_pieces_list)
        self.black_pieces_list_history = utils.copier_objet(self.black_pieces_list)
        try:
            id_piece, move_piece = move
            if color == "white":
                for index, piece in enumerate(self.white_pieces_list):
                    if piece.id == id_piece:
                        self.white_pieces_list[index].pos_x, self.white_pieces_list[index].pos_y = move_piece
            if color == "black":
                for index, piece in enumerate(self.black_pieces_list):
                    if piece.id == id_piece:
                        self.black_pieces_list[index].pos_x, self.black_pieces_list[index].pos_y = move_piece
            self.updatePion()
            self.updateBoard(color)
            self.verifyBoard()
            self.gameOver(color)
        except TypeError:
            print(f'valeur problème de move:{move}')
        
    
    def undoMove(self, color):
        self.white_pieces_list = self.white_pieces_list_history
        self.black_pieces_list = self.black_pieces_list_history
        self.updateBoard(color)


    def eval(self, color):
        list_piece1 = self.white_pieces_list if color == "white" else self.black_pieces_list
        list_piece2 = self.black_pieces_list if color == "white" else self.white_pieces_list

        score_piece_number = 10 if len(list_piece1) < len(list_piece2) else -10 # score positif si le nombre de pièce est inférieur à celui de l'adversaire
        score_piece_value = 10 if sum([piece.value for piece in list_piece2]) > sum([piece.value for piece in list_piece1]) else -10 # score positif si la valeur totale des pièces est inférieure à celle de l'adversaire
        score_capture_number = len(self.pieceFirstMoves(list_piece2)) * 5 # plus il y a de capture possible par l'adversaire plus le score est important

        if len(list_piece1) < 8 and self.size == 8 or len(list_piece1) < 6 and self.size == 6 : # l'importance des captures et du nombres de pièces augmentent
            score_capture_number *= 2
            score_piece_number *= 2
            if any(piece.name in ["BQ", "NQ"] for piece in list_piece1):
                score_piece_value -= 5
        elif len(list_piece1) < 4:
            score_capture_number *= 4
            score_piece_number *= 4
        if len(list_piece1) <= 1 and score_capture_number != 0: # suicide move pour gagner
            return 9999
        
        return score_piece_number + score_piece_value + score_capture_number

    def gameOver(self, color):
        if (color == "white" and len(self.black_pieces_list) == 0 or 
        len(self.pieceSecondMoves(self.black_pieces_list)) == 0 and len(self.pieceFirstMoves(self.black_pieces_list)) == 0):
            self.game_over = "Black"
            # print("Black Win")
        if (color == "black" and len(self.white_pieces_list) == 0 or 
        len(self.pieceSecondMoves(self.white_pieces_list)) == 0 and len(self.pieceFirstMoves(self.white_pieces_list)) == 0):
            self.game_over = "White"
            # print("White Win")

class Board8x8(Board):
    def __init__(self) -> None:
        super().__init__(8)
        
    
    def initPiece(self):
        index_id = 0
        piece_list = {
        "NT": Piece.Tour,
        "BT": Piece.Tour,
        "NF": Piece.Fou,
        "BF": Piece.Fou,
        "NC": Piece.Cavalier,
        "BC": Piece.Cavalier,
        "NQ": Piece.Reine,
        "BQ": Piece.Reine,
        "NK": Piece.Roi,
        "BK": Piece.Roi,
        "BP": Piece.Pion,
        "NP": Piece.Pion
        }
        for row in range(self.size):
            for col in range(self.size):
                piece_name = self.board[row][col]
                if piece_name in piece_list:
                    piece_class = piece_list[piece_name]
                    new_piece = piece_class(piece_name, row, col, index_id, self)
                    index_id += 1
                    if "B" in piece_name:
                        self.white_pieces_list.append(new_piece)
                    else:
                        self.black_pieces_list.append(new_piece)

    def initBoard(self):
        self.board = [["NT","NC","NF","NQ","NK","NF","NC","NT"],
                      ["NP","NP","NP","NP","NP","NP","NP","NP"],
                      ["__","__","__","__","__","__","__","__"],
                      ["__","__","__","__","__","__","__","__"],
                      ["__","__","__","__","__","__","__","__"],
                      ["__","__","__","__","__","__","__","__"],
                      ["BP","BP","BP","BP","BP","BP","BP","BP"],
                      ["BT","BC","BF","BQ","BK","BF","BC","BT"]]
        
class Board6x6(Board):
    def __init__(self) -> None:
        super().__init__(6)
        
        
    def initPiece(self):
        index_id = 0
        piece_list = {
        "NT": Piece.Tour,
        "BT": Piece.Tour,
        "NC": Piece.Cavalier,
        "BC": Piece.Cavalier,
        "NQ": Piece.Reine,
        "BQ": Piece.Reine,
        "NK": Piece.Roi,
        "BK": Piece.Roi,
        "BP": Piece.Pion,
        "NP": Piece.Pion
        }
        for row in range(self.size):
            for col in range(self.size):
                piece_name = self.board[row][col]
                if piece_name in piece_list:
                    piece_class = piece_list[piece_name]
                    new_piece = piece_class(piece_name, row, col, index_id, self)
                    index_id += 1
                    if "B" in piece_name:
                        self.white_pieces_list.append(new_piece)
                    else:
                        self.black_pieces_list.append(new_piece)
    
    def initBoard(self):
        self.board = [["NT","NC","NQ","NK","NC","NT"],
                      ["NP","NP","NP","NP","NP","NP"],
                      ["__","__","__","__","__","__"],
                      ["__","__","__","__","__","__"],
                      ["BP","BP","BP","BP","BP","BP"],
                      ["BT","BC","BQ","BK","BC","BT"]]