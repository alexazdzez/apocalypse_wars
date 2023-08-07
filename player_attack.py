import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.game = game
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 20

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        for monster in pygame.sprite.spritecollide(self, self.game.all_monsters, False, pygame.sprite.collide_mask):
            self.remove()
            monster.damage(self.player.attack)
        if self.rect.x == 1200:
            self.remove()