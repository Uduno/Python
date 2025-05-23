import pygame
from config import HEIGHT, WIDTH, WHITE, ORANGE

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


class Popup:
    def __init__(self, text, buttons, font, size=(400, 200)):
        self.rect = pygame.Rect((WIDTH // 2 - size[0] // 2, HEIGHT // 2 - size[1] // 2), size)
        self.text = font.render(text, True, WHITE)
        self.buttons = buttons
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, (ORANGE), self.rect)
        screen.blit(self.text, (self.rect.centerx - self.text.get_width() // 2, self.rect.top + 20))
        for btn in self.buttons:
            btn.draw(screen)

    def handle_event(self, event):
        for btn in self.buttons:
            btn.handle_event(event)
