import pygame
from config import WIDTH, HEIGHT, p_speed

class Player():
    def __init__(self):
        self.hp = 3
        self.img = pygame.image.load("assets/vaisseau.png") # chargement de l'image
        self.rect = self.img.get_rect()
        self.rect.x = (WIDTH - self.rect.width) // 2 # pos x
        self.rect.y = HEIGHT - self.rect.height # pos y
    
    def move_right(self): # mouvement à droite
        if self.rect.right < WIDTH:
            self.rect.x += p_speed

    def move_left(self): # mouvement à gauche
        if self.rect.left > 0:
            self.rect.x -= p_speed

    def draw(self, surface): # dessin 
        surface.blit(self.img, self.rect)

