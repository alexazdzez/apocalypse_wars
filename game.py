import pygame
from player import Player
from enemies import Monster


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
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
        self.is_playing = False


    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        self.player.update_health_bar(screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.all_monsters.draw(screen)



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
        self.all_monsters.add(Monster(self))

    def addscore(self, add):
        self.score += add

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

