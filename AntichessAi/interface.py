import pygame
import board 


# Pygame
pygame.init()  # Initialisation

white = (226, 213, 161)  # couleur case blanche
black = (120, 79, 70)  # couleur case noire 
list_img = {}


def chargeImg(): # chargement des images des pièces
    list_name = ["NT","NC","NF","NQ","NK","NP","BT","BC","BF","BQ","BK","BP"]
    for name in list_name:
        list_img[name] = (pygame.image.load(f'assets/{name}.png'))


class Interface():
    def __init__(self, screen, page) -> None:
        self.screen = screen
        self.screen_size = 640 # taille de l'écran width & height
        self.page = page
    
    def draw(self):
        pass

    def action(self, event):
        pass

class chooseSizeBoard(Interface):
    def __init__(self, screen) -> None:
        super().__init__(screen, 1)

    def draw(self):
        self.screen.fill(white)
        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render("Choix taille du plateau", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 50)))
        pygame.draw.rect(self.screen, black, (200, 150, 240, 100),2)
        text = font.render("8 x 8", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 200)))
        pygame.draw.rect(self.screen, black, (200, 350, 240, 100),2)
        text = font.render("6 x 6", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 400)))

    def action(self, event):
         if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 200 <= x <= 440 and 150 <= y <= 250:
                return chooseAi(self.screen, 8)
            if 200 <= x <= 440 and 350 <= y <= 450:
                return chooseAi(self.screen, 6)
            
class chooseAi(Interface):
    def __init__(self, screen, format) -> None:
        super().__init__(screen, 2)
        self.format = format
        self.white_ai = None
        self.black_ai = None
    
    def draw(self):
        self.screen.fill(white)
        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render("Choix Ai", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 50)))
        text = font.render("White", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 4, 100)))
        text = font.render("Black", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size - self.screen_size // 4, 100)))
        text = font.render("Random", True, white if self.white_ai == 1 else black)
        pygame.draw.rect(self.screen, black , (50, 160, 220, 80),2  if self.white_ai != 1 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 4, 200)))
        text = font.render("Random", True, white if self.black_ai == 1 else black)
        pygame.draw.rect(self.screen, black , (365, 160, 220, 80),2  if self.black_ai != 1 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size - self.screen_size // 4, 200)))
        text = font.render("MiniMax", True, white if self.white_ai == 2 else black)
        pygame.draw.rect(self.screen, black , (50, 260, 220, 80),2  if self.white_ai != 2 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 4, 300)))
        text = font.render("MiniMax", True, white if self.black_ai == 2 else black)
        pygame.draw.rect(self.screen, black , (365, 260, 220, 80),2  if self.black_ai != 2 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size - self.screen_size // 4, 300)))
        text = font.render("AlphaBeta", True, white if self.white_ai == 3 else black)
        pygame.draw.rect(self.screen, black , (50, 360, 220, 80),2  if self.white_ai != 3 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 4, 400)))
        text = font.render("AlphaBeta", True, white if self.black_ai == 3 else black)
        pygame.draw.rect(self.screen, black , (365, 360, 220, 80),2  if self.black_ai != 3 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size - self.screen_size // 4, 400)))
        text = font.render("MTCT", True, white if self.white_ai == 4 else black)
        pygame.draw.rect(self.screen, black , (50, 460, 220, 80),2  if self.white_ai != 4 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 4, 500)))
        text = font.render("MTCT", True, white if self.black_ai == 4 else black)
        pygame.draw.rect(self.screen, black , (365, 460, 220, 80),2  if self.black_ai != 4 else 0)
        self.screen.blit(text, text.get_rect(center = (self.screen_size - self.screen_size // 4, 500)))
        text = font.render("Confirmer", True, white)
        pygame.draw.rect(self.screen, black , (210, 560, 220, 80))
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 600)))
    
    def action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 50<= x <= 270 and 160 <= y <= 240:
                self.white_ai = 1
            if 50<= x <= 270 and 260 <= y <= 340:
                self.white_ai = 2
            if 50<= x <= 270 and 360 <= y <= 440:
                self.white_ai = 3
            if 50<= x <= 270 and 460 <= y <= 540:
                self.white_ai = 4
            if 365<= x <= 585 and 160 <= y <= 240:
                self.black_ai = 1
            if 365<= x <= 585 and 260 <= y <= 340:
                self.black_ai = 2
            if 365<= x <= 585 and 360 <= y <= 440:
                self.black_ai = 3
            if 365<= x <= 585 and 460 <= y <= 540:
                self.black_ai = 4
            
            if 210 <= x <= 430 and 560 <= y <= 640:
                if self.black_ai != None and self.white_ai != None:
                    return boardGame(self.screen, self.format, self.white_ai, self.black_ai)

class boardGame(Interface):
    def __init__(self, screen, format, ai_white, ai_black) -> None:
        super().__init__(screen, 3)
        self.format = format
        self.ai_white = ai_white
        self.ai_black = ai_black
        self.square_size = self.screen_size // self.format
        self.board = board.Board8x8() if format == 8 else board.Board6x6()

    def draw(self):
        for row in range(self.format):
            for col in range(self.format):
                color = white if (row + col) % 2 == 0 else black
                pygame.draw.rect(self.screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
                piece =  self.board.board[row][col]
                if piece != "__":
                    size = self.screen_size/ self.format
                    img = pygame.transform.scale(list_img[piece],(size, size))
                    self.screen.blit(img, (col * size, row * size))        

        pygame.display.update()
    
    def action(self, event):
        if self.board.game_over != None:
            return endPAge(self.screen, self.format, self.ai_white, self.ai_black, self.board.game_over)
        
class endPAge(Interface):
    def __init__(self, screen, format, ai_white, ai_black, winner) -> None:
        super().__init__(screen, 4)
        self.format = format
        self.ai_white = ai_white
        self.ai_black = ai_black
        self.winner = winner

    def draw(self):
        self.screen.fill(white)
        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render(f'{self.winner} Victory', True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 50)))
        pygame.draw.rect(self.screen, black, (200, 150, 240, 100),2)
        text = font.render("Relancer", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 200)))
        pygame.draw.rect(self.screen, black, (200, 350, 240, 100),2)
        text = font.render("Changer", True, black)
        self.screen.blit(text, text.get_rect(center = (self.screen_size // 2, 400)))
    
    def action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 200 <= x <= 440 and 150 <= y <= 250:
                return boardGame(self.screen, self.format, self.ai_white, self.ai_black)
            if 200 <= x <= 440 and 350 <= y <= 450:
                return chooseSizeBoard(self.screen)

# # initialisation de l'écran
# screen = pygame.display.set_mode((640, 640))
# pygame.display.set_caption("Antichess")

# # initialisation de la page 1
# page = endPAge(screen, 1,1,1,1)

# clock = pygame.time.Clock()
# running = True
# TIMER_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(TIMER_EVENT, 1500)
# turn = 0
# chargeImg()
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     next_page = page.action(event)
#     if next_page:
#             page = next_page
#     # affichage de la page actuelle
#     page.draw()    

#     # maj de l'écran
#     pygame.display.flip()

# pygame.quit()