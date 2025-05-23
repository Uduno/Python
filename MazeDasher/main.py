import pygame
import sys
from ui import Button
from config import *
from menu import Menu, Controls

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Principal")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

menu = Menu(screen, font)
controls =  Controls(screen, font)
current_state = "menu"
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_state == "menu":
            current_state = menu.handle_event(event)
            menu.draw()
        if current_state == "controls":
            current_state = controls.handle_event(event)
            controls.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()
