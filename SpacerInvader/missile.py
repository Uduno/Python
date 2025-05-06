import pygame
from config import m_size, m_speed

class Missile():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, m_size, m_size)
    
    def move(self, side):
        self.rect.y += m_speed * side # side negatif si c'est le joueur, positif si c'est l'ennemi

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)
        
