import pygame, sys
from player import Player
from missile import Missile
from config import *

pygame.init()

player = Player()
player_missile = []
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")



def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)  
        screen.fill(WHITE)

        keys  = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_LEFT]:
            player.move_left()


        for missile in player_missile[:]:
            missile.move(-1)
            if missile.rect.bottom < 0:
                player_missile.remove(missile)
            missile.draw(screen, BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    missile_x = player.rect.centerx - (m_size/2)
                    missile_y = player.rect.top
                    player_missile.append(Missile(missile_x, missile_y))
        


        
        player.draw(screen)
        pygame.display.flip()
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
