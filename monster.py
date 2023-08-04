import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.velocity = 2
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 550


    def update_health_bar(self, surface):
        bar_color = (51, 222, 77)
        bar_position = [self.rect.x, self.rect.y, self.health, 5]

        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_colision(self, self.game.all_players):
            self.rect.x -= self.velocity