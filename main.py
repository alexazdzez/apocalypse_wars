import pygame
from game import Game

pygame.init()


iconapp = pygame.image.load('assets/icon.png')
pygame.display.set_caption("Apocalypse Wars")
pygame.display.set_icon(iconapp)
screen = pygame.display.set_mode((1230, 670))

background = pygame.image.load('assets/bg.jpg')
game = Game()
#
running = True

while running:

    screen.blit(background, (0, 0))

    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()

    game.player.all_projectiles.draw(screen)

    game.all_monsters.draw(screen)


    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1100:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_SPACE):
        if game.score < 100:
            game.projectile_boost = True
            game.player.launch_projectile()
        else:
            game.projectile_boost = False

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
