import pygame
from config import HEIGHT, WIDTH, WHITE, ORANGE, BLACK

class Button:
    def __init__(self, text, pos, size, callback, font, color=(WHITE), bg=(ORANGE)):
        self.rect = pygame.Rect(pos, size)
        self.text = font.render(text, True, color)
        self.text_pos = self.text.get_rect(center=self.rect.center)
        self.callback = callback
        self.bg = bg

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, self.rect)
        screen.blit(self.text, self.text_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.callback:
                self.callback()
            return True

