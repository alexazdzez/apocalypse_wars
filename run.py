import math
import pygame
import pickle
from game import Game

pygame.init()

clock = pygame.time.Clock()
#todo fix fps
#todo create mega boss
#todo fix life/difficulty
#todo best score
#todo create fraction for kill
#todo fix tank crash
FPS = 2048

pygame.display.set_caption("Apocalypse Wars")
screen = pygame.display.set_mode((1230, 670))

background = pygame.image.load('assets/bg.jpg')

playbt = pygame.transform.scale(pygame.image.load('assets/button.png'), (400, 150))

settingbt = pygame.transform.scale(pygame.image.load('assets/setting.jpeg'), (100, 55))

difficultybt = pygame.transform.scale(pygame.image.load('assets/difficulty.png'), (200, 200))

playbt_rect = playbt.get_rect()
playbt_rect.x = math.ceil(screen.get_width() / 3.33)
playbt_rect.y = math.ceil(screen.get_height() / 1.8)

settingbt_rect = settingbt.get_rect()
settingbt_rect.x = 0
settingbt_rect.y = 620

difficultybt_rect = settingbt.get_rect()
difficultybt_rect.x = math.ceil(screen.get_width() / 2.5)
difficultybt_rect.y = math.ceil(screen.get_height() / 2.5)

game = Game()

running = True
try:
    file = open('assets/saves/save', 'rb')
    sauvegarde = pickle.load(file)
    game.difficulty = sauvegarde[0]
    game.best_score = sauvegarde[1]

    game.last_killed_zombie = sauvegarde[2]
    game.last_killed_tank = sauvegarde[3]

    game.best_killed_zombie = sauvegarde[4]
    game.best_killed_tank = sauvegarde[5]
    file.close()
except:
    pass
font = pygame.font.SysFont("monospace", 16)
best_score_text = font.render(f"Best score : {game.best_score}", 1, (0, 0, 0))
last_killed_zombie_text = font.render(f"last killed zombie : {game.last_killed_zombie}", 1, (0, 0, 0))
last_killed_tank_text = font.render(f"last killed tank : {game.last_killed_tank}", 1, (0, 0, 0))
best_killed_zombie_text = font.render(f"best killed zombie : {game.best_killed_zombie}", 1, (0, 0, 0))
best_killed_tank_text = font.render(f"best killed tank : {game.best_killed_tank}", 1, (0, 0, 0))
while running:

    screen.blit(background, (0, 0))

    if game.is_playing == 1:
        game.update(screen)
    elif game.is_playing == 2:
        font = pygame.font.SysFont("monospace", 16)

        difficulty_text = font.render(f"difficulty : {game.difficulty}", 1, (0, 0, 0))
        help_difficulty_text = font.render(f"1 = easy, 2 = normal, 3 = hard, 4 = extreme, 5 = gamer", 1, (0, 0, 0))

        screen.blit(difficulty_text, (200, 20))
        screen.blit(help_difficulty_text, (200, 40))

        screen.blit(difficultybt, difficultybt_rect)
    else:
        screen.blit(playbt, playbt_rect)
        screen.blit(settingbt, settingbt_rect)
        screen.blit(best_score_text, (100, 40))
        screen.blit(last_killed_zombie_text, (100, 60))
        screen.blit(last_killed_tank_text, (100, 80))
        screen.blit(best_killed_zombie_text, (100, 100))
        screen.blit(best_killed_tank_text, (100, 120))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game.is_playing == 1:
                    game.game_over()
                elif game.is_playing == 2:
                    game.is_playing = 0
                else:
                    running = False
                    pygame.quit()
            elif event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playbt_rect.collidepoint(event.pos) and game.is_playing == 0:
                game.start()
            elif settingbt_rect.collidepoint(event.pos) and game.is_playing == 0:
                game.setting()
            elif difficultybt_rect.collidepoint(event.pos) and game.is_playing == 2:
                if game.difficulty == 1:
                    game.difficulty = 2
                elif game.difficulty == 2:
                    game.difficulty = 3
                elif game.difficulty == 3:
                    game.difficulty = 4
                elif game.difficulty == 4:
                    game.difficulty = 5
                elif game.difficulty == 5:
                    game.difficulty = 1

    clock.tick(FPS)
