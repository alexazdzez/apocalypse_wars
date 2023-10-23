import pygame

from run import game


class Tank(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.loot = 10
        self.velocity = 1
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load('assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 550

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.add_score(self.loot)
            if game.difficulty == 1:
                self.game.player.add_projectile(4)
            if game.difficulty == 2:
                self.game.player.add_projectile(3)
            if game.difficulty == 3:
                self.game.player.add_projectile(2)
            if game.difficulty == 4:
                self.game.player.add_projectile(1)
            if game.difficulty == 5:
                self.game.player.add_projectile(0.5)
            self.game.all_tanks.remove(self)
            self.game.spawn_monster()
            self.game.restart_cycle()
            self.game.spawn_monster()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 70, self.rect.y + 5, self.max_health, 5])
        pygame.draw.rect(surface, (51, 222, 77), [self.rect.x + 70, self.rect.y + 5, self.health, 5])

    def forward(self):
        if not pygame.sprite.spritecollide(self, self.game.all_players, False, pygame.sprite.collide_mask):
            self.rect.x -= self.velocity
        self.game.player.damage(self.attack)
