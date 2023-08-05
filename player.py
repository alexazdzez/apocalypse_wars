import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 150
        self.normal_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.normal_rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 550
        self.normal_rect.x = 500
        self.normal_rect.y = 550

    def damage(self, amount):
        self.health -= amount
        if self.game.chance >= 1:
            if self.health <= 0:
                self.game.chance -= 1
                self.health = self.normal_health
        elif self.health <= 0:
            self.game.game_over()


    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.normal_health, 5])
        pygame.draw.rect(surface, (51, 222, 77), [self.rect.x + 10, self.rect.y - 10, self.health, 5])

    def move_right(self):
        if not self.game.check_colision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    #
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
