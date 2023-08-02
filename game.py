import pygame
from player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}
        self.score = 0
        self.projectile_boost = True
#