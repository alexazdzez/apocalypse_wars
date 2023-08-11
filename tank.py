import pygame


class Tank(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.velocity = 1
        self.game = game
        self.loot = 10
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.image.load('assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 550

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.add_score(self.loot)
            self.game.all_tanks.remove(self)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 70, self.rect.y + 5, self.max_health, 5])
        pygame.draw.rect(surface, (51, 222, 77), [self.rect.x + 70, self.rect.y + 5, self.health, 5])

    def forward(self):
        if not pygame.sprite.spritecollide(self, self.game.all_players, False, pygame.sprite.collide_mask):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
