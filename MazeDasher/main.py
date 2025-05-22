import pygame, sys
from config import *
from level_reader import read_level
from player import Player

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
mid_rows = (16 - rows) / 2
mid_cols = (16 - cols) / 2

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            tile = level[row][col]
            if tile in tile_map:
                screen.blit(tile_map[tile], ( (col + mid_cols)* TILE_SIZE  , (row - mid_rows) * TILE_SIZE + WIDTH))

for row in range(rows):
        for col in range(cols):
            tile = level[row][col]
            if tile == "S":
                player = Player(col , row)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)  
        screen.fill(GREEN)


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.dashing(1, 0, level)
                if event.key == pygame.K_LEFT:
                    player.dashing(-1, 0, level)
                if event.key == pygame.K_UP:
                    player.dashing(0, -1, level)
                if event.key == pygame.K_DOWN:
                    player.dashing(0, 1, level)
                if event.key == pygame.K_SPACE:
                    player.transformation()

        draw_grid()
        player.move()
        player.draw(screen, level)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
