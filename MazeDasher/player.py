import pygame
from config import TILE_SIZE, TILES_CHAR, WIDTH, ANIMALS

class Player:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.real_x = pos_x * TILE_SIZE
        self.real_y = pos_y * TILE_SIZE
        self.speed = 8
        self.direction = "down"
        self.dash = False
        self.transforming = False
        self.animal_index = 0
        self.anim_index = 0
        self.time_anim = pygame.time.get_ticks()
        self.anim_delay = 100
        self.idle_anim = self.load_anim(f'assets/spritesheets/{ANIMALS[self.animal_index]}', 4)
        self.dash_anim = self.load_anim("assets/spritesheets/dash.png", 4)
        self.transfo_anim = self.load_anim("assets/spritesheets/transformation.png", 8)
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
            self.time_anim = time_t

            if self.anim_index + 1 >= len(self.anim):
                if self.transforming:
                    self.finish_transformation()
                else:
                    self.anim_index = 0
            else:
                self.anim_index += 1



    def transformation(self):
        if not self.transforming:
            self.transforming = True
            self.anim = self.transfo_anim
            self.anim_index = 0
            self.time_anim = pygame.time.get_ticks()

    def finish_transformation(self):
        self.transforming = False
        self.animal_index = (self.animal_index + 1) % len(ANIMALS)
        self.idle_anim = self.load_anim(f'assets/spritesheets/{ANIMALS[self.animal_index]}', 4)
        self.anim = self.idle_anim
        self.anim_index = 0



    def get_rotation(self):
        sprite = self.anim[self.anim_index]
        rotate = {"down": 0, "right": 90, "up": 180, "left": -90}[self.direction]
        return pygame.transform.rotate(sprite, rotate)
    
    def draw(self, screen, level):
        self.update_anim()
        sprite = self.get_rotation()
        mid_rows = (16 - len(level))// 2
        mid_cols = (16 - len(level[0])) // 2
        x = self.real_x + mid_cols * TILE_SIZE
        y = self.real_y - mid_rows * TILE_SIZE + WIDTH
        screen.blit(sprite, (x , y ))

    def dashing(self, x, y, level):
        if self.dash or self.transforming:
            return 
        self.dash = True
        self.anim = self.dash_anim
        self.dash_direction = (x, y)

        while True:
            new_x = self.x + x
            new_y = self.y + y
            if not self.can_move(new_x, new_y, level):
                break
            self.x = new_x
            self.y = new_y

        direction_map = {(1, 0): "right", (0, 1): "down", (-1, 0): "left", (0, -1): "up"}
        self.direction = direction_map[(x, y)]

    def can_move(self, x, y, level):
        if y < 0 or y >= len(level) or x < 0 or x >= len(level[0]):
            return False
        return level[y][x] not in TILES_CHAR

    def move(self):
        if self.dash:
            end_x = self.x * TILE_SIZE - self.real_x
            end_y = self.y * TILE_SIZE - self.real_y

            if abs(end_x) <= self.speed and abs(end_y) <= self.speed:
                self.real_x = self.x * TILE_SIZE
                self.real_y = self.y * TILE_SIZE
                self.anim = self.idle_anim
                self.anim_index = 0
                self.dash = False
                
            else:
                self.real_x += self.speed * ( 1 if end_x > 0 else -1 if end_x < 0 else 0 )
                self.real_y += self.speed * ( 1 if end_y > 0 else -1 if end_y < 0 else 0 )