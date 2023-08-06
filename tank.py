import pygame


class Tank:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/tank.png')
        self.rect = self.image.get_rect()
