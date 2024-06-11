import pygame
import interface
import time
import ai

# Pygame
pygame.init()  # Initialisation
# initialisation de l'écran
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Antichess")

# initialisation de la page 1
page = interface.chooseSizeBoard(screen)

clock = pygame.time.Clock()
running = True
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1500)
turn = 0
interface.chargeImg()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if page.page == 3:
            color = "white" if turn % 2 == 0 else "black"
            color_ai = page.ai_white if color == "white" else page.ai_black
            move = ai.aiChoose(color_ai, page.board, color, 1.5)
            page.board.makeMove(move, color)
            #on garde l'historique des coups joués
            page.board.moves_history.append(move)
            print(color,move)
            # print(color, page.board.eval(color), move)
            page.board.showBoard()
            turn += 1
        next_page = page.action(event)
        if next_page:
                page = next_page
        # affichage de la page actuelle
        page.draw()    

    # maj de l'écran
    pygame.display.flip()

pygame.quit()