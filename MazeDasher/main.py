import pygame, sys
from config import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MazeDasher")


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)  
        screen.fill(GREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
