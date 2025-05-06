import pygame
import random
from config import e_speed, e_down, WIDTH
class Ennemy():
    def __init__(self, x, y, speed):
        self.img = pygame.image.load(f'assets/alien_{random.randint(1, 3)}.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = e_speed + speed
    
    def move(self):
        self.rect.x += self.direction * self.speed
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += e_down

    def draw(self, surface):
        surface.blit(self.img, self.rect)