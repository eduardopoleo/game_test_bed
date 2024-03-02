# TODO:
# make the snail move to the left 
# Add jump and gravity
# remap this cgn to something a bit easier 
# set list by default in neovim config

import pygame
import sys
import random
from objects.enemy import Enemy
from objects.player import Player
from objects.obstacle import Obstacle

class Game:
    FPS = 60
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Jumper Game")

        # TODO: Maybe the images path can be stracted into constants
        # along with other game settings like the FPS later

        self.ground_img = pygame.image.load('graphics/Ground.png').convert()
        self.sky_img = pygame.image.load('graphics/Sky.png').convert()

        self.player_images = [
            pygame.image.load('graphics/Player/player_stand.png').convert_alpha(),
            pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(),
            pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha(),
            pygame.image.load('graphics/Player/jump.png').convert_alpha()
        ]

        self.snail_images = [
            pygame.image.load('graphics/snail/snail1.png').convert_alpha(),
            pygame.image.load('graphics/snail/snail2.png').convert_alpha()
        ]

        self.fly_images = [
            pygame.image.load('graphics/Fly/Fly1.png').convert_alpha(),
            pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
        ]

        self.enemies = []

        self.obstacles = pygame.sprite.Group()  

        ground = Obstacle(self.screen, self.ground_img, (0, 300))
        print(f"ground {ground.rect}")
        self.obstacles.add(ground)

        platform_img1 = pygame.Surface((200, 50))
        platform_img1.fill((255, 0, 0))
        platform1 = Obstacle(self.screen, platform_img1, (400, 200))
        self.obstacles.add(platform1)

        platform_img2 = pygame.Surface((200, 50))
        platform_img2.fill((255, 0, 0))
        platform2 = Obstacle(self.screen, platform_img2, (400, 50))
        self.obstacles.add(platform2)

        self.player = Player(self.player_images, self.screen, self.obstacles)
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)

    def run(self):
        clock = pygame.time.Clock()

        current_time = pygame.time.get_ticks() / 1000
        initial_time = pygame.time.get_ticks() / 1000

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Updating player velocities directly from here is buggy
                # it's best to just update the direction and they use that number
                # to update the velocity in the player class. Not sure why this is.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not self.player.moving_vertically():
                        self.player.start_jump()
                    if event.key == pygame.K_RIGHT:
                        self.player.direction[0] += 1
                    if event.key == pygame.K_LEFT:
                        self.player.direction[0] -= 1
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player.direction[0] -= 1
                    if event.key == pygame.K_LEFT:
                        self.player.direction[0] += 1

            self.screen.blit(self.sky_img, (0, 0))
            # self.obstacles.draw(self.screen)

            current_time = pygame.time.get_ticks() / 1000
            time_elapsed = current_time - initial_time

            if time_elapsed >= Enemy.SPAWN_INTERVAL:
                initial_time = current_time
                enemy_type = random.choice(['fly', 'snail'])
                new_enemy = None
                if enemy_type == 'snail':
                    new_enemy = Enemy(self.screen, 300, self.snail_images)
                else:
                    new_enemy = Enemy(self.screen, 200, self.fly_images)

                self.enemies.append(new_enemy)

            self.player_group.update()
            self.player_group.draw(self.screen)
            self.obstacles.draw(self.screen)

            for enemy in self.enemies:
                if enemy.rect.x < -200:
                    enemies_to_remove = enemy
                else:
                    enemy.update()
                    # enemy.render()
 
            pygame.display.update()

            clock.tick(Game.FPS)

game = Game()
game.run()

