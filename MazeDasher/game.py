import pygame, sys
from config import *
from level_reader import read_level
from player import Player
from ui import Button

class Game():
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.levels = LEVEL
        self.level_index = 0
        self.level = None
        self.player = None
        self.pause_buttons = []
        self.end_buttons = []
        self.load_level(self.level_index)  

    def load_level(self, index):
        self.level_index = index
        self.level = read_level(f'assets/levels/{self.levels[index]}')
        self.player = self.init_player()
        self.create_buttons()  

    def load_next_level(self):
        if self.level_index + 1 < len(self.levels):
            self.load_level(self.level_index + 1)
            return True
        return False

    def init_player(self):
        for y, row in enumerate(self.level):
            for x, tile in enumerate(row):
                if tile == "S":
                    return Player(x, y)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "pause"
            if event.key == pygame.K_SPACE:
                self.player.transformation()
            if not self.player.dash:
                if event.key == pygame.K_UP:
                    self.player.dashing(0, -1, self.level)
                elif event.key == pygame.K_DOWN:
                    self.player.dashing(0, 1, self.level)
                elif event.key == pygame.K_LEFT:
                    self.player.dashing(-1, 0, self.level)
                elif event.key == pygame.K_RIGHT:
                    self.player.dashing(1, 0, self.level)

        return "play"

    def draw(self):
        self.screen.fill(GREEN)
        self.draw_level()
        self.player.move()
        self.player.draw(self.screen, self.level)

        if self.is_level_complete():
            return "completed"
        return "play"

    def draw_level(self):
        tile_map = {}
        for char, file in TILES.items():
            path = TILES_PATH + file
            image = pygame.image.load(path).convert_alpha()
            tile_map[char] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

        rows = len(self.level)
        cols = len(self.level[0])
        mid_cols = (16 - cols) // 2

        for row in range(rows):
            for col in range(cols):
                tile = self.level[row][col]
                x = (col + mid_cols) * TILE_SIZE
                y = row * TILE_SIZE
                pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                if tile in tile_map:
                    self.screen.blit(tile_map[tile], (x, y))

    def is_level_complete(self):
        x, y = self.player.x, self.player.y
        return self.level[y][x] == "X"

    def create_buttons(self):
        self.pause_buttons = [
            Button("Continuer", (WIDTH // 2 - 100, 250), (200, 50), None, self.font),
            Button("Recommencer", (WIDTH // 2 - 100, 300), (200, 50), None, self.font),
            Button("Menu", (WIDTH // 2 - 100, 350), (200, 50), None, self.font),
        ]
        self.end_buttons = [
            Button("Niveau Suivant", (WIDTH // 2 - 100, 250), (200, 50), None, self.font),
            Button("Menu", (WIDTH // 2 - 100, 325), (200, 50), None, self.font),
        ]

    def handle_popup(self, events, popup_type):
        buttons = self.pause_buttons if popup_type == "pause" else self.end_buttons
        for event in events:
            for btn in buttons:
                result = btn.handle_event(event)
                if result:
                    return result
        return popup_type

    def draw_popup(self, popup_type):
        pygame.draw.rect(self.screen, BLACK, (150, 180, 500, 250))
        text = "Pause" if popup_type == "pause" else "Niveau Terminé"
        label = self.font.render(text, True, WHITE)
        self.screen.blit(label, (WIDTH // 2 - label.get_width() // 2, 200))

        buttons = self.pause_buttons if popup_type == "pause" else self.end_buttons
        for btn in buttons:
            btn.draw(self.screen)


        
        
        
    def handle_pause_popup(self, events):
        for event in events:
            if self.pause_buttons[0].handle_event(event):
                return "play"
            if self.pause_buttons[1].handle_event(event):
                return "restart"
            if self.pause_buttons[2].handle_event(event):
                return "menu"

    def handle_end_popup(self, events):
        for event in events:
            if self.end_buttons[0].handle_event(event):
                return "next"
            if self.end_buttons[1].handle_event(event):
                return "menu"

    def draw_pause_popup(self):
        self.draw_popup("pause")

    def draw_end_popup(self):
        self.draw_popup("end")

# pygame.init()

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("MazeDasher")

# tile_map = {}
# for char, file in TILES.items():
#     path = TILES_PATH + file
#     image = pygame.image.load(path).convert_alpha()
#     tile_map[char] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

# level = read_level("assets/levels/level_10.txt")
# rows = len(level)
# cols = len(level[0])
# mid_rows = (16 - rows) // 2
# mid_cols = (16 - cols) // 2

# def draw_grid(screen):
#     for row in range(rows):
#         for col in range(cols):
#             tile = level[row][col]
#             x = (col + mid_cols) * TILE_SIZE
#             y = row  * TILE_SIZE
#             pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1 )
#             if tile in tile_map:
#                 screen.blit(tile_map[tile], (x, y))
                


# for row in range(rows):
#         for col in range(cols):
#             tile = level[row][col]
#             if tile == "S":
#                 player = Player(col , row)

# def main():
#     clock = pygame.time.Clock()
#     running = True

#     while running:
#         clock.tick(60)  
#         screen.fill(GREEN)


        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RIGHT:
#                     player.dashing(1, 0, level)
#                 if event.key == pygame.K_LEFT:
#                     player.dashing(-1, 0, level)
#                 if event.key == pygame.K_UP:
#                     player.dashing(0, -1, level)
#                 if event.key == pygame.K_DOWN:
#                     player.dashing(0, 1, level)
#                 if event.key == pygame.K_SPACE:
#                     player.transformation()

#         draw_grid(screen)
#         player.move()
#         player.draw(screen, level)
        
#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()
