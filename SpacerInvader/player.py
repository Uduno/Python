import pygame
from config import WIDTH, HEIGHT, p_speed

class Player():
    def __init__(self):
        self.hp = 3
        self.img = pygame.image.load("assets/vaisseau.png")
        self.rect = self.img.get_rect()
        self.rect.x = (WIDTH - self.rect.width) // 2
        self.rect.y = HEIGHT - self.rect.height
    
    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.x += p_speed

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= p_speed

    def draw(self, surface):
        surface.blit(self.img, self.rect)

    def get_position(self):
        return self.rect.x, self.rect.y