import pygame
import random
import time

# Définir la taille de la fenêtre
width, height = 800, 600

class MemoryGame:
    def __init__(self):
        self.card_list = [1, 2, 3] # liste des cartes
        self.board = [] # tableau du jeu
        self.state_board = [] # état du tableau
        self.img_list = {} # dictionnaire des images
        self.chosen_card = [None, None] # choix de cartes
        self.card_width = 126 # largeur d'une carte (largeur réel: 360)
        self.card_height = 224 # hauteur d'une carte (hauteur réel: 640)
        self.create_board()
        self.init_img_list()

    def create_board(self):
        tmp_board = self.card_list * 2 # 2 fois le tableau card_list
        random.shuffle(tmp_board) # melange le tableau tmp_board
        for i in range(2):  # on ajoute 2 fois
            row = tmp_board[i*3:i*3+3]  # on ajoute 3 cartes
            self.state_board.append([0, 0, 0])    
            self.board.append(row) # on ajoute une ligne

    def init_img_list(self): # Initiliasation de l'image des cartes
        list_file = ["Card_Back.png", "Card_1.png", "Card_2.png", "Card_3.png"] 
        for index, file in enumerate(list_file):
            self.img_list[index] = pygame.image.load("assets/" + file) 

    def draw_board(self, screen): # Affichage du jeu
        # Effacer l'écran
        screen.fill((255, 255, 255))
        # Afficher le titre "Memory" centré en haut
        font = pygame.font.Font(None, 36)
        text = font.render("Memory", True, (0, 0, 0))
        text_rect = text.get_rect(center=(width/2, 40))
        screen.blit(text, text_rect)

        # Afficher les cartes en grille 3x2
        x_spacing = 20
        y_spacing = 20
        x_start = (width - 3 * (self.card_width + x_spacing)) / 2
        y_start = 100
        for i in range(2):
            for j in range(3):
                card = self.board[i][j] if self.state_board[i][j] != 0 else 0  # valeur de la carte si la carte est visible, sinon 0
                card_image = pygame.transform.scale(self.img_list[card], (self.card_width, self.card_height))  # Redimensionner l'image
                screen.blit(card_image, (x_start + j * (self.card_width + x_spacing), y_start + i * (self.card_height + y_spacing)))
                card_rect = pygame.Rect(x_start + j * (self.card_width + x_spacing), y_start + i * (self.card_height + y_spacing), self.card_width, self.card_height)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if card_rect.collidepoint(x, y):
                        row = int((y - y_start) / (self.card_height + y_spacing))
                        col = int((x - x_start) / (self.card_width + x_spacing))
                        if self.state_board[row][col] == 0 :
                            print(row, col, self.board)
                            self.flip_card(row, col)
            
    def flip_card(self, row, col): # Méthode pour changer l'etat d'une carte
        if self.chosen_card[0] is None:
            self.chosen_card[0] = row, col, self.board[row][col]
            self.state_board[row][col] = 1
        else:
            self.chosen_card[1] = row, col, self.board[row][col]
            self.state_board[row][col] = 1
            if self.chosen_card[0][2] == self.chosen_card[1][2]:
                self.chosen_card = [None, None]
            else:
                row1, col1, _ = self.chosen_card[0]
                row2, col2, _ = self.chosen_card[1]
                pygame.time.wait(500)
                self.state_board[row1][col1] = 0
                self.state_board[row2][col2] = 0
                self.chosen_card = [None, None]


pygame.init()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Memory")
game = MemoryGame()

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.draw_board(screen)
    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()