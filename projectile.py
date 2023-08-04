import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 20

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if self.player.game.check_colision(self, self.player.game.all_monsters) or self.rect.x + self.velocity > 1100:
            self.remove()
        else:
            self.rect.x += self.velocity