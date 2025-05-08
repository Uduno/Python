import pygame
import random
from config import e_speed, e_down, WIDTH

class Ennemy():
    def __init__(self, x, y, speed): # pos x, pos y et vitesse
        self.img = pygame.image.load(f'assets/alien_{random.randint(1, 3)}.png') # Charge une image parmi les 3 dispos pour l'alien
        self.rect = self.img.get_rect() # 
        self.rect.x = x
        self.rect.y = y
        self.direction = 1 # change en fonction du deplacement gauche ou droite (1 ou -1)
        self.speed = e_speed + speed
    
    def move(self): # deplacement 
        self.rect.x += self.direction * self.speed 
        if self.rect.right >= WIDTH or self.rect.left <= 0: # si l'alien touche un bord à gauche ou à droite
            self.direction *= -1
            self.rect.y += e_down # descente

    def draw(self, surface):
        surface.blit(self.img, self.rect)