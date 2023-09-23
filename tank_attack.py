import pygame


class Obus(pygame.sprite.Sprite):

    def __init__(self, tank, game):
        super().__init__()
        self.velocity = 2
        self.tank = tank
        self.game = game
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
        self.rect.x = tank.rect.x + 120
        self.rect.y = tank.rect.y + 20

    def remove(self):
        self.tank.all_obus.remove(self)

    def move(self):
        self.rect.x -= self.velocity
        for player in pygame.sprite.spritecollide(self, self.game.all_players, False, pygame.sprite.collide_mask):
            self.remove()
            player.damage(self.tank.attack)
        if self.rect.x == 1200:
            self.remove()