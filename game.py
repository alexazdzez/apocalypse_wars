import pygame
from player import Player
from tank import Tank
from tank_event import TankEntranceEvent
from enemies import Enemies


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.tank = Tank(self)
        self.all_players.add(self.player)
        self.all_tanks = pygame.sprite.Group()
        self.TankEntranceEvent = TankEntranceEvent(self)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.normal_chance = 2
        self.chance = 2
        self.is_playing = False

    def start(self):
        self.is_playing = True
        self.player.rect = self.player.normal_rect
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.normal_health
        self.chance = self.normal_chance
        self.TankEntranceEvent.percent = 0
        self.score = 0
        self.is_playing = False


    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move()
        for obus in self.tank.all_obus:
            obus.move()

        self.player.all_projectiles.draw(screen)

        self.tank.all_obus.draw(screen)


        self.player.update_health_bar(screen)

        self.TankEntranceEvent.update_bar(screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.all_monsters.draw(screen)

        self.all_tanks.draw(screen)
        for tank in self.all_tanks:
            tank.forward()
            tank.update_health_bar(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1100:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        pygame.display.flip()


    def spawn_monster(self):
        self.all_monsters.add(Enemies(self))

    def spawn_tank(self):
        self.all_tanks.add(Tank(self))

    def add_score(self, add):
        self.score += add

    def restart_cycle(self):
        self.TankEntranceEvent.is_wait = False

