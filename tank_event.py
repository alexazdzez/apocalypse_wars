import pygame
from tank import Tank


class TankEntranceEvent:
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5
        self.all_tanks = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def tanks_entrance(self):
        self.percent = 0
    def attempt_tank(self):
        if self.is_full_loaded():
            self.reset_percent()
            self.tanks_entrance()

    def update_bar(self, surface):
        self.addpercent()
        self.attempt_tank()
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height(),
            surface.get_width() - 10,
            10
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 10,
            (surface.get_width() / 100) * self.percent,
            10
        ])