import pygame
import math
from game import Game

pygame.init()

clock = pygame.time.Clock()
FPS = 512

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
#
running = True

while running:

    screen.blit(background, (0, 0))

    if game.is_playing == 1:
        game.update(screen)
    elif game.is_playing == 2:
        font = pygame.font.SysFont("monospace", 16)

        difficulty_text = font.render(f"difficulty : {game.difficulty}", 1, (0, 0, 0))
        help_difficulty_text = font.render(f"1 = easy, 2 = normal, 3 = hard, 4 = extreme", 1, (0, 0, 0))

        screen.blit(difficulty_text, (200, 20))
        screen.blit(help_difficulty_text, (200, 40))

        screen.blit(difficultybt, difficultybt_rect)
    else:
        screen.blit(playbt, playbt_rect)
        screen.blit(settingbt, settingbt_rect)

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
                    game.difficulty = 1

    clock.tick(FPS)