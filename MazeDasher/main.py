import pygame, sys
from config import *
from level_reader import read_level

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MazeDasher")


tile_map = {}
for char, file in TILES.items():
    path = TILES_PATH + file
    tile_map[char] = pygame.image.load(path)

level = read_level("assets/levels/level_01.txt")
rows = len(level)
cols = len(level[0])

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            tile = level[row][col]
            if tile in tile_map:
                screen.blit(tile_map[tile], (col * 32, row * 32))

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)  
        screen.fill(GREEN)


        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
