import pygame


class TankEntranceEvent:
    def __init__(self, game):
        self.game = game
        self.percent = 1
        self.is_wait = False
        self.nb_cycle = 1
        self.percent_speed = 5 + self.nb_cycle
        self.all_tanks = pygame.sprite.Group()
        self.tank_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def tanks_entrance(self):
        self.game.spawn_tank()

    def attempt_tank(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.reset_percent()
            self.nb_cycle += 1
            self.game.before_boss -= 1
            if self.game.before_boss <= 0:
                print("mega boss")
                self.game.before_boss = 6
            else:
                self.game.killed_zombie += len(self.game.all_monsters)
                self.tank_mode = True
                self.tanks_entrance()
        elif self.is_full_loaded():
            self.is_wait = True



    def update_bar(self, surface):
        self.add_percent()
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
