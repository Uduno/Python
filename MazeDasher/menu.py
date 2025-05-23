import pygame
from ui import Button
from config import *

class Menu():
    def __init__(self, screen, font):
        self.screen = screen
        self.start_btn = Button("Jouer", (WIDTH // 2 - 75, 325), (150, 50), None, font)
        self.show_command_btn = Button("Commandes", (WIDTH // 2 - 75, 425), (150, 50), None, font)

    def handle_event(self, event):
        if self.start_btn.handle_event(event):
            return "play"
        if self.show_command_btn.handle_event(event):
            return "controls"    
            
        return "menu"
    
    def draw(self):
        self.screen.fill(GREEN)
        self.start_btn.draw(self.screen)
        self.show_command_btn.draw(self.screen)



class Controls():
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.return_button = Button("Retour", (WIDTH // 2 - 75, 500), (150, 50), None, font)

    def handle_event(self, event):
        if self.return_button.handle_event(event):
            return "menu"
        return "controls"

    def draw(self):
        self.screen.fill(GREEN)


        panel_rect = pygame.Rect(200, 150, 400, 300)
        pygame.draw.rect(self.screen, BLACK, panel_rect)

        title_surf = self.font.render("Commandes", True, WHITE)
        self.screen.blit(title_surf, (panel_rect.centerx - title_surf.get_width() // 2, panel_rect.y + 10))


        commands = [
            "Flèches : Se déplacer",
            "Espace : Se transformer",
            "Échap : Ouvrir le menu"
        ]

        for i, line in enumerate(commands):
            text_surf = self.font.render(line, True, WHITE)
            self.screen.blit(text_surf, (panel_rect.x + 20, panel_rect.y + 60 + i * 40))


        self.return_button.draw(self.screen)


