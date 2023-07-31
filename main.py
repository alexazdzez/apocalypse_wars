import pygame
from game import Game

pygame.init()


iconapp = pygame.image.load('assets/icon.png')
pygame.display.set_caption("Apocalypse Wars")
pygame.display.set_icon(iconapp)
screen = pygame.display.set_mode((1280, 670))

background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

while running:

    screen.blit(background, (25, 0))

    screen.blit(game.player.image, game.player.rect)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
