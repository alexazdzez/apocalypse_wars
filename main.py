import pygame
import math
from game import Game

pygame.init()


iconapp = pygame.image.load('assets/icon.png')
pygame.display.set_caption("Apocalypse Wars")
pygame.display.set_icon(iconapp)
screen = pygame.display.set_mode((1230, 670))

background = pygame.image.load('assets/bg.jpg')

playimg = pygame.transform.scale(pygame.image.load('assets/banner.png'), (500, 500))

playimg_rect = playimg.get_rect()
playimg_rect.x = math.ceil(screen.get_width() / 4)

playbt = pygame.transform.scale(pygame.image.load('assets/button.png'), (400, 150))

playbt_rect = playbt.get_rect()
playbt_rect.x = math.ceil(screen.get_width() / 3.33)
playbt_rect.y = math.ceil(screen.get_height() / 1.8)

game = Game()
#
running = True

while running:

    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(playbt, playbt_rect)
        screen.blit(playimg, playimg_rect)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.projectile_boost == False:
                game.player.launch_projectile()
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playbt_rect.collidepoint(event.pos):
                game.start()
