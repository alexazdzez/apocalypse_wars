import pygame


class TankEntranceEvent:
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5

    def addpercent(self):
        self.percent += self.percent_speed / 100

    def update_bar(self, surface):
        self.addpercent()
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