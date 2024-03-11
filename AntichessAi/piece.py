# Pièces du jeu

class Piece():
    def __init__(self, name, pos_x, pos_y, id, board, value) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id
        self.board = board
        self.value = value
    
    def moves(self):
        return [],[]
    


class Roi(Piece):
    def __init__(self, name, pos_x, pos_y, id, board) -> None:
        super().__init__(name, pos_x, pos_y, id, board, 5)

    def moves(self):
        first_moves_list = []  # liste des coups prioritaires (capture)
        second_moves_list = []  # liste des coups secondaires (pas de capture)
        # liste des mouvements du roi
        moves_list = [
            [self.pos_x + 1, self.pos_y], [self.pos_x, self.pos_y + 1],
            [self.pos_x - 1, self.pos_y], [self.pos_x, self.pos_y - 1],
            [self.pos_x + 1, self.pos_y + 1], [self.pos_x - 1, self.pos_y - 1],
            [self.pos_x + 1, self.pos_y - 1], [self.pos_x - 1, self.pos_y + 1]
        ]

        for move in moves_list:
            pos_xt, pos_yt = move
            if 0 <= pos_xt < self.board.size and 0 <= pos_yt < self.board.size:
                if self.board.board[pos_xt][pos_yt] == "__": # si la case est vide
                    second_moves_list.append((self.id, [pos_xt, pos_yt]))
                else:
                    if (self.name[0] not in self.board.board[pos_xt][pos_yt]): # si le 1er caractère diffère -> pièce à capturer
                        first_moves_list.append((self.id, [pos_xt, pos_yt])) 
        
        return first_moves_list, second_moves_list
    

class Reine(Piece):
    def __init__(self, name, pos_x, pos_y, id, board) -> None:
        super().__init__(name, pos_x, pos_y, id, board, 6)

    def moves(self):
        first_moves_list = []  # liste des coups prioritaires (capture)
        second_moves_list = []  # liste des coups secondaires (pas de capture)


        for case in range(1, self.board.size+1):
            if self.pos_x + case < self.board.size:
                if self.board.board[self.pos_x + case][ self.pos_y] == "__":
                    second_moves_list.append((self.id, [self.pos_x + case, self.pos_y]))  # déplacement vers le bas
                else:
                    if self.name[0] not in self.board.board[self.pos_x + case][ self.pos_y]:
                        first_moves_list.append((self.id, [self.pos_x + case, self.pos_y]))  # capture vers le bas
                    break

        for case in range(1, self.pos_x + 1):
            if self.pos_x > 0:
                if self.board.board[self.pos_x - case][ self.pos_y] == "__":
                    second_moves_list.append((self.id, [self.pos_x - case, self.pos_y]))  # déplacement vers le haut
                else: 
                    if self.name[0] not in self.board.board[self.pos_x - case][ self.pos_y]:
                        first_moves_list.append((self.id, [self.pos_x - case, self.pos_y]))  # capture vers le haut
                    break

        for case in range(1, self.pos_y + 1):
            if self.pos_y > 0:
                if self.board.board[self.pos_x ][ self.pos_y - case] == "__":
                    second_moves_list.append((self.id, [self.pos_x, self.pos_y - case]))  # déplacement vers la gauche
                else: 
                    if self.name[0] not in self.board.board[self.pos_x ][ self.pos_y - case]:
                        first_moves_list.append((self.id, [self.pos_x, self.pos_y - case]))  # capture vers la gauche
                    break

        for case in range(1, self.board.size+1):
            if self.pos_y + case < self.board.size:
                if self.board.board[self.pos_x][self.pos_y + case] == "__":
                    second_moves_list.append((self.id, [self.pos_x, self.pos_y + case]))  # déplacement vers la droite
                else:
                    if self.name[0] not in self.board.board[self.pos_x][self.pos_y + case]:
                        first_moves_list.append((self.id, [self.pos_x, self.pos_y + case]))  # capture vers la droite
                    break
        
        for case in range(1, min(self.pos_x, self.pos_y) + 1):
            if self.board.board[self.pos_x - case][self.pos_y - case] == "__":
                second_moves_list.append((self.id, [self.pos_x - case, self.pos_y - case]))  # déplacement vers le haut à gauche
            else:
                if self.name[0] not in self.board.board[self.pos_x - case][self.pos_y - case]:
                    first_moves_list.append((self.id, [self.pos_x - case, self.pos_y - case])) # capture vers le haut à gauche
                break

        for case in range(1, min(self.pos_x + 1, self.board.size - self.pos_y) ):
            if self.board.board[self.pos_x - case][self.pos_y + case] == "__":
                second_moves_list.append((self.id, [self.pos_x - case, self.pos_y + case])) # déplacement vers le haut à droite
            else:
                if self.name[0] not in self.board.board[self.pos_x - case][self.pos_y + case]:
                    first_moves_list.append((self.id, [self.pos_x - case, self.pos_y + case])) # capture vers le haut à droite
                break
                


        for case in range(1, min(self.board.size - self.pos_x, self.pos_y + 1)):
            if self.board.board[self.pos_x + case][self.pos_y - case] == "__":
                second_moves_list.append((self.id, [self.pos_x + case, self.pos_y - case])) # déplacement vers le bas à gauche
            else:
                if self.name[0] not in self.board.board[self.pos_x + case][self.pos_y - case]:
                    first_moves_list.append((self.id, [self.pos_x + case, self.pos_y - case])) # capture vers le bas à gauche
                break
 
        for case in range(1, min(self.board.size - self.pos_x, self.board.size - self.pos_y)):
            if self.board.board[self.pos_x + case][self.pos_y + case] == "__":
                second_moves_list.append((self.id, [self.pos_x + case, self.pos_y + case])) # déplacement vers le bas à droite 
            else:
                if self.name[0] not in self.board.board[self.pos_x + case][self.pos_y + case]:
                    first_moves_list.append((self.id, [self.pos_x + case, self.pos_y + case])) # capture vers le bas à droite
                break


        return first_moves_list, second_moves_list

class Tour(Piece):
    def __init__(self, name, pos_x, pos_y, id, board) -> None:
        super().__init__(name, pos_x, pos_y, id, board, 5)

    def moves(self):
        first_moves_list = []  # liste des coups prioritaires (capture)
        second_moves_list = []  # liste des coups secondaires (pas de capture)

        for case in range(1, self.board.size+1):
            if self.pos_x + case < self.board.size:
                if self.board.board[self.pos_x + case][self.pos_y] == "__":
                    second_moves_list.append((self.id, [self.pos_x + case, self.pos_y]))  # déplacement vers le bas
                else:
                    if self.name[0] not in self.board.board[self.pos_x + case][ self.pos_y]:
                        first_moves_list.append((self.id, [self.pos_x + case, self.pos_y]))  # capture vers le bas
                    break

        for case in range(1, self.pos_x + 1):
            if self.pos_x > 0:
                if self.board.board[self.pos_x - case][ self.pos_y] == "__":
                    second_moves_list.append((self.id, [self.pos_x - case, self.pos_y]))  # déplacement vers le haut
                else: 
                    if self.name[0] not in self.board.board[self.pos_x - case][ self.pos_y]:
                        first_moves_list.append((self.id, [self.pos_x - case, self.pos_y]))  # capture vers le haut
                    break

        for case in range(1, self.pos_y + 1):
            if self.pos_y > 0:
                if self.board.board[self.pos_x ][ self.pos_y - case] == "__":
                    second_moves_list.append((self.id, [self.pos_x, self.pos_y - case]))  # déplacement vers la gauche
                else: 
                    if self.name[0] not in self.board.board[self.pos_x ][ self.pos_y - case]:
                        first_moves_list.append((self.id, [self.pos_x, self.pos_y - case]))  # capture vers la gauche
                    break

        for case in range(1, self.board.size+1):
            if self.pos_y + case < self.board.size:
                if self.board.board[self.pos_x][self.pos_y + case] == "__":
                    second_moves_list.append((self.id, [self.pos_x, self.pos_y + case]))  # déplacement vers la droite
                else:
                    if self.name[0] not in self.board.board[self.pos_x][self.pos_y + case]:
                        first_moves_list.append((self.id, [self.pos_x, self.pos_y + case]))  # capture vers la droite
                    break
        
        return first_moves_list, second_moves_list

class Fou(Piece):
    def __init__(self, name, pos_x, pos_y, id, board) -> None:
        super().__init__(name, pos_x, pos_y, id, board, 3)

    def moves(self):
        first_moves_list = []  # liste des coups prioritaires (capture)
        second_moves_list = []  # liste des coups secondaires (pas de capture)

        for case in range(1, min(self.pos_x, self.pos_y) + 1):
            if self.board.board[self.pos_x - case][self.pos_y - case] == "__":
                second_moves_list.append((self.id, [self.pos_x - case, self.pos_y - case]))  # déplacement vers le haut à gauche
            else:
                if self.name[0] not in self.board.board[self.pos_x - case][self.pos_y - case]:
                    first_moves_list.append((self.id, [self.pos_x - case, self.pos_y - case])) # capture vers le haut à gauche
                break

        for case in range(1, min(self.pos_x + 1, self.board.size - self.pos_y) ):
            if self.board.board[self.pos_x - case][self.pos_y + case] == "__":
                second_moves_list.append((self.id, [self.pos_x - case, self.pos_y + case])) # déplacement vers le haut à droite
            else:
                if self.name[0] not in self.board.board[self.pos_x - case][self.pos_y + case]:
                    first_moves_list.append((self.id, [self.pos_x - case, self.pos_y + case])) # capture vers le haut à droite
                break
                
        for case in range(1, min(self.board.size - self.pos_x, self.pos_y + 1)):
            if self.board.board[self.pos_x + case][self.pos_y - case] == "__":
                second_moves_list.append((self.id, [self.pos_x + case, self.pos_y - case])) # déplacement vers le bas à gauche
            else:
                if self.name[0] not in self.board.board[self.pos_x + case][self.pos_y - case]:
                    first_moves_list.append((self.id, [self.pos_x + case, self.pos_y - case])) # capture vers le bas à gauche
                break
 
        for case in range(1, min(self.board.size - self.pos_x, self.board.size - self.pos_y)):
            if self.board.board[self.pos_x + case][self.pos_y + case] == "__":
                second_moves_list.append((self.id, [self.pos_x + case, self.pos_y + case])) # déplacement vers le bas à droite 
            else:
                if self.name[0] not in self.board.board[self.pos_x + case][self.pos_y + case]:
                    first_moves_list.append((self.id, [self.pos_x + case, self.pos_y + case])) # capture vers le bas à droite
                break

        return first_moves_list, second_moves_list
    
class Cavalier(Piece):
    def __init__(self, name, pos_x, pos_y, id, board) -> None:
        super().__init__(name, pos_x, pos_y, id, board, 3)

    def moves(self):
        first_moves_list = []  # liste des coups prioritaires (capture)
        second_moves_list = []  # liste des coups secondaires (pas de capture)
        # listes des mouvements du cavalier
        moves_list = [
            [self.pos_x + 2, self.pos_y + 1], [self.pos_x + 2, self.pos_y  - 1],
            [self.pos_x + 1, self.pos_y + 2], [self.pos_x - 1, self.pos_y  + 2],
            [self.pos_x - 2, self.pos_y + 1], [self.pos_x - 2, self.pos_y  - 1],
            [self.pos_x + 1, self.pos_y - 2], [self.pos_x - 1, self.pos_y  - 2],
        ]

        for move in moves_list:
            pos_xt, pos_yt = move
            if 0 <= pos_xt < self.board.size and 0 <= pos_yt < self.board.size:
                if self.board.board[pos_xt][pos_yt] == "__": # si la case est vide
                    second_moves_list.append((self.id, [pos_xt, pos_yt]))
                else:
                    if self.name[0] not in self.board.board[pos_xt][pos_yt]: # si le 1er caractère diffère -> pièce à capturer
                        first_moves_list.append((self.id, [pos_xt, pos_yt])) 
        
        return first_moves_list, second_moves_list
    
class Pion(Piece):
    def __init__(self, name, pos_x, pos_y, id, board) -> None:
        super().__init__(name, pos_x, pos_y, id, board, 1)

    def moves(self):
        first_moves_list = []  # liste des coups prioritaires (capture)
        second_moves_list = []  # liste des coups secondaires (pas de capture)

        
        if self.name[0] == "B":
            if self.pos_x > 0 and self.board.board[self.pos_x - 1][self.pos_y] == "__":
                if self.pos_x == self.board.size - 2 and self.board.board[self.pos_x - 2][self.pos_y] == "__":
                    second_moves_list.append((self.id, [self.pos_x - 2, self.pos_y])) # avance de 2 cases
                second_moves_list.append((self.id, [self.pos_x - 1, self.pos_y])) # avance de 1 case

            if self.pos_x > 0 and self.pos_y < self.board.size - 1 and "N" in self.board.board[self.pos_x - 1][self.pos_y + 1]:
                first_moves_list.append((self.id, [self.pos_x - 1, self.pos_y + 1])) # capture en diagonale droit
            if self.pos_x > 0 and self.pos_y > 0 and "N" in self.board.board[self.pos_x - 1][self.pos_y - 1]:
                first_moves_list.append((self.id, [self.pos_x - 1, self.pos_y - 1])) # capture en diagonale gauche

        else: 
            if self.pos_x < self.board.size - 1 and self.board.board[self.pos_x + 1][self.pos_y] == "__":
                if self.pos_x == 1 and self.board.board[self.pos_x + 2][self.pos_y] == "__":
                    second_moves_list.append((self.id, [self.pos_x + 2, self.pos_y])) # avance de 2 cases
                second_moves_list.append((self.id, [self.pos_x + 1, self.pos_y])) # avance de 1 case


            if self.pos_x < self.board.size - 1 and self.pos_y < self.board.size - 1 and "B" in self.board.board[self.pos_x + 1][self.pos_y + 1]:
                first_moves_list.append((self.id, [self.pos_x + 1, self.pos_y + 1])) # capture en diagonale gauche
            if self.pos_x < self.board.size - 1 and self.pos_y > 0 and "B" in self.board.board[self.pos_x + 1][self.pos_y - 1]:
                first_moves_list.append((self.id, [self.pos_x + 1, self.pos_y - 1])) # capture en diagonale droite

        return first_moves_list, second_moves_list