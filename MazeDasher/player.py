import pygame
from config import TILE_SIZE, TILES_CHAR, WIDTH

class Player:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.direction = "down"
        self.dash = False
        self.anim_index = 0
        self.time_anim = pygame.time.get_ticks()
        self.anim_delay = 100
        self.idle_anim = self.load_anim("assets/spritesheets/cow.png", 4)
        self.dash_anim = self.load_anim("assets/spritesheets/dash.png", 4)

        self.anim = self.idle_anim

    def load_anim(self, path, nb_sprite):
        spritesheet = pygame.image.load(path)
        width_sprite = spritesheet.get_width() // nb_sprite
        sprites = []
        for i in range(nb_sprite):
            sprite = spritesheet.subsurface(pygame.Rect(i * width_sprite, 0, width_sprite, spritesheet.get_height()))
            sprites.append(sprite)
        return sprites    
        
    def update_anim(self):
        time_t = pygame.time.get_ticks()
        if time_t - self.time_anim >= self.anim_delay:
            self.anim_index = (self.anim_index + 1)% len(self.anim)
            self.time_anim = time_t
    
    def get_rotation(self):
        sprite = self.anim[self.anim_index]
        rotate = {"down": 0, "right": 90, "up": 180, "left": -90}[self.direction]
        return pygame.transform.rotate(sprite, rotate)
    
    def draw(self, screen, level):
        self.update_anim()
        sprite = self.get_rotation()
        mid_rows = (16 - len(level))// 2
        mid_cols = (16 - len(level[0])) // 2
        x = (self.x + mid_cols) * TILE_SIZE
        y = (self.y - mid_rows) * TILE_SIZE + WIDTH
        
        screen.blit(sprite, (x , y ))

    def dashing(self, x, y, level):
        self.dash = True
        self.anim = self.dash_anim
        direction_map = {(1, 0): "right", (0, 1): "down", (-1, 0): "left", (0, -1): "up"}
        self.direction = direction_map[(x, y)]

        while True:
            new_x = self.x + x
            new_y = self.y + y
            if not self.can_move(new_x, new_y, level):
                break
            self.x = new_x
            self.y = new_y

        self.dash = False
        self.anim = self.idle_anim
        self.anim_index = 0

    def can_move(self, x, y, level):
        print(self.x, self.y, x, y)
        if y < 0 or y >= len(level) or x < 0 or x >= len(level[0]):
            return False
        return level[y][x] not in TILES_CHAR
