import pygame
from player import Player
from tank import Tank
import pickle
from tank_event import TankEntranceEvent
from enemies import Enemies


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.spawned_zombie = 0
        self.tank = Tank(self)
        self.all_players.add(self.player)
        self.best_score = 0
        self.before_boss = 6
        self.killed_zombie = 0
        self.killed_tank = 0
        self.best_killed_zombie = 0
        self.best_killed_tank = 0
        self.difficulty = 2
        self.all_tanks = pygame.sprite.Group()
        self.TankEntranceEvent = TankEntranceEvent(self)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.is_playing = 0
        self.chance = 3

    def start(self):
        if self.difficulty == 1:
            self.chance = 3
        elif self.difficulty == 2:
            self.chance = 2
        elif self.difficulty == 3:
            self.chance = 2
        elif self.difficulty == 4:
            self.chance = 1
        elif self.difficulty == 5:
            self.chance = 0
        self.killed_zombie = 0
        self.killed_tank = 0
        self.is_playing = 1
        self.player.rect = self.player.normal_rect
        if self.difficulty == 1:
            self.spawn_monster()
            self.spawn_monster()
            self.spawned_zombie += 2
        elif self.difficulty == 2:
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawned_zombie += 3
        elif self.difficulty == 3:
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawned_zombie += 4
        elif self.difficulty == 4:
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawned_zombie += 6
        elif self.difficulty == 5:
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawn_monster()
            self.spawned_zombie += 4
            self.spawn_tank()

    def setting(self):
        self.is_playing = 2

    def game_over(self):
        self.save()
        self.all_monsters = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.health = self.player.normal_health
        self.TankEntranceEvent.percent = 0
        self.score = 0
        self.is_playing = 0

    def save(self):
        file = open('assets/saves/save', 'wb')
        sauvegarde = [
            self.difficulty,
            self.best_score,
            self.best_killed_zombie,
            self.best_killed_tank
        ]
        pickle.dump(sauvegarde, file)
        file.close()

    def update(self, screen):

        if self.killed_zombie > self.best_killed_zombie:
            self.best_killed_zombie = self.killed_zombie
        if self.killed_tank > self.best_killed_tank:
            self.best_killed_tank = self.killed_tank
        if self.score > self.best_score:
            self.best_score = self.score

        font = pygame.font.SysFont("monospace", 16)

        killed_zombie_text = font.render(f"killed zombie : {self.killed_zombie}", 1, (0, 0, 0))
        killed_tank_text = font.render(f"killed tank : {self.killed_tank}", 1, (0, 0, 0))
        best_killed_zombie_text = font.render(f"best killed zombie : {self.best_killed_zombie}", 1, (0, 0, 0))
        best_killed_tank_text = font.render(f"best killed tank : {self.best_killed_tank}", 1, (0, 0, 0))
        life_text = font.render(f"life : {self.chance + 1}", 1, (0, 0, 0))
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        best_score_text = font.render(f"Best score : {self.best_score}", 1, (0, 0, 0))
        rocket_ammo_text = font.render(f"rocket ammo : {self.player.rocket_ammo}", 1, (0, 0, 0))
        zombie_fraction_text = font.render(f"you killed : {self.killed_zombie} / {self.spawned_zombie}", 1, (0, 0, 0))

        screen.blit(score_text, (100, 20))
        screen.blit(best_score_text, (100, 40))
        screen.blit(rocket_ammo_text, (100, 60))
        screen.blit(killed_zombie_text, (100, 80))
        screen.blit(killed_tank_text, (100, 100))
        screen.blit(best_killed_zombie_text, (100, 120))
        screen.blit(best_killed_tank_text, (100, 140))
        screen.blit(life_text, (100, 160))
        screen.blit(zombie_fraction_text, (100, 180))

        self.all_monsters.draw(screen)
        self.all_tanks.draw(screen)
        self.player.all_projectiles.draw(screen)
        self.player.update_health_bar(screen)
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for tank in self.all_tanks:
            tank.forward()
            tank.update_health_bar(screen)
        self.TankEntranceEvent.update_bar(screen)

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
