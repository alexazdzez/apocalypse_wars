import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 540
        self.velocity = 1

    def forward(self):
        self.rect.x -= self.velocity
