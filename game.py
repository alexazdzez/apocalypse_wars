import pygame
from player import Player
from monster import Monster


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.projectile_boost = True
        self.spawn_monster()
        self.spawn_monster()

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def addscore(self, add):
        self.score += add

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

