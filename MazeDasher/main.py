import pygame
import sys
from ui import Button
from config import *
from menu import Menu, Controls
from game import Game

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Principal")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

menu = Menu(screen, font)
controls = Controls(screen, font)
game = Game(screen, font)

current_state = "menu"
running = True

while running:
    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if current_state == "menu":
        for event in events:
            result = menu.handle_event(event)
            if result == "play":
                game.load_level(0)
                current_state = "play"
            elif result == "controls":
                current_state = "controls"
        menu.draw()

    elif current_state == "controls":
        for event in events:
            result = controls.handle_event(event)
            if result == "menu":
                current_state = "menu"
        controls.draw()

    elif current_state == "play":
        for event in events:
            result = game.handle_event(event)
            if result == "pause":
                current_state = "pause"
        state = game.draw()  # Important : `draw()` renvoie "play" ou "completed"
        if state == "completed":
            current_state = "end"

    elif current_state == "pause":
        game.draw()
        game.draw_pause_popup()
        action = game.handle_pause_popup(events)
        if action == "resume":
            current_state = "play"
        elif action == "restart":
            game.load_level(game.level_index)
            current_state = "play"
        elif action == "menu":
            current_state = "menu"

    elif current_state == "end":
        game.draw()
        game.draw_end_popup()
        action = game.handle_end_popup(events)
        if action == "next":
            if game.load_next_level():
                current_state = "play"
            else:
                current_state = "menu"
        elif action == "menu":
            current_state = "menu"

    pygame.display.flip()

pygame.quit()
sys.exit()
