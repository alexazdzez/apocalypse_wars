import pygame
from player import Player
from tank_event import TankEntranceEvent
from enemies import Enemies


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_tanks = pygame.sprite.Group
        self.TankEntranceEvent = TankEntranceEvent(self)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.normal_chance = 2
        self.chance = 2
        self.is_playing = False
        self.projectile_boost = True

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
        self.is_playing = True


    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        self.player.update_health_bar(screen)

        self.TankEntranceEvent.update_bar(surface=screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.all_monsters.draw(screen)

        self.TankEntranceEvent.all_tanks.draw(screen)
        self.TankEntranceEvent.update()
        self.all_tanks.f

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1100:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_SPACE):
            if self.score < 100:
                self.projectile_boost = True
                self.player.launch_projectile()
            else:
                if 300 < self.score < 500:
                    self.projectile_boost = True
                    self.player.launch_projectile()
                else:
                    self.projectile_boost = False

        pygame.display.flip()


    def spawn_monster(self):
        self.all_monsters.add(Enemies(self))

    def add_score(self, add):
        self.score += add

    def check_colision(self, group2):
        return pygame.sprite.spritecollide(self, group2, False, pygame.sprite.collide_mask)

