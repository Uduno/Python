import pygame, sys, random
from player import Player
from missile import Missile
from ennemy import Ennemy
from config import *

pygame.init()

player = Player()
player_missile = []

life = pygame.image.load("assets/life.png") # image de coeur
# font d'ecriture
font = pygame.font.SysFont('assets/minecraft_font.ttf', 15) 
font2 = pygame.font.SysFont('assets/minecraft_font.ttf', 40)

ennemies = [] # liste d'ennemis
ennemi_missile = [] # liste des missiles ennemi
last_shoot = 0 
delai_shoot = 1500 #1.5s delai de tir
lines = 3
cols = 6

actual_speed = e_speed

def invasion(speed): # fonction de création de vagues ennemi
    for line in range(lines):
        for col in range(cols):
            x = 60 + col * 30
            y = 30 + line * 30
            ennemies.append(Ennemy(x, y, speed))
invasion(actual_speed)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spacer Invader")



def main():
    global actual_speed, last_shoot
    score = 0
    gameover = False
    clock = pygame.time.Clock()
    

    running = True

    while running:
        clock.tick(60)  
        actual_time = pygame.time.get_ticks()
        screen.fill(WHITE)

        # affichage du score
        score_draw = font.render(f'{int(score)}', True, BLACK)
        score_rec = score_draw.get_rect()
        score_rec.topright = (WIDTH - 10, 10)
        screen.blit(score_draw, score_rec)

        # affichage du gameover
        if gameover == True:
           gameover_text1 = font2.render("Game Over", True, BLACK)
           gameover_text2 = font2.render("Press 'Enter'", True, BLACK)
           text1_rect = gameover_text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
           text2_rect = gameover_text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
           screen.blit(gameover_text1, text1_rect)
           screen.blit(gameover_text2, text2_rect)


        # touche de déplacement du joueur
        keys  = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_LEFT]:
            player.move_left()

        for hp in range(player.hp):
            screen.blit(life,(hp * 20, 7.5))

        # gestion des missiles du joueur
        for missile in player_missile[:]:
            missile.move(-1)
            if missile.rect.bottom < 0:
                player_missile.remove(missile)
            for ennemi in ennemies[:]:
                if ennemi.rect.colliderect(missile.rect):
                    player_missile.remove(missile)
                    ennemies.remove(ennemi)
                    score += 100 * actual_speed
                    break
            if ennemies == []:
                if actual_speed < 3:
                    actual_speed += 0.2
                invasion(actual_speed)
            missile.draw(screen, BLUE)

        # gestion des ennemis
        for ennemi in ennemies[:]:
            if gameover != True:
                ennemi.move()
                if ennemi.rect.colliderect(player.rect):
                    gameover = True
                ennemi.draw(screen)

        # gestion des missiles ennemi
        for missile in ennemi_missile[:]:
            missile.move(1)
            if missile.rect.top > HEIGHT:
                ennemi_missile.remove(missile)
                break
            if missile.rect.colliderect(player.rect):
                player.hp -= 1
                ennemi_missile.remove(missile)
                if player.hp <= 0:
                    gameover = True
                break
            missile.draw(screen, RED)
        
        # gestion du tir d'un missile ennemi
        if actual_time - last_shoot >= delai_shoot and gameover != True:
            index_ennemi = random.randrange(len(ennemies))
            missile_x = ennemies[index_ennemi].rect.centerx - (m_size/2)
            missile_y = ennemies[index_ennemi].rect.bottom
            ennemi_missile.append(Missile(missile_x, missile_y))
            last_shoot = actual_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # tir du joueur en appuyant sur "espace"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    missile_x = player.rect.centerx - (m_size/2)
                    missile_y = player.rect.top
                    player_missile.append(Missile(missile_x, missile_y))
                # relancer le jeu apres un gameover
                if event.key == pygame.K_RETURN and gameover == True:
                    gameover = False
                    actual_speed = 1
                    score = 0
                    player.hp = 3
                    ennemies.clear()
                    player_missile.clear()
                    ennemi_missile.clear()
                    invasion(actual_speed)


        
        player.draw(screen)
        pygame.display.flip()
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
