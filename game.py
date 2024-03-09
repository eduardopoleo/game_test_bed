# TODO:
# Remove the usage of silly sprites and make everything lists
# Remove the pictures and make eveything based on blocks
# Calculate the collissions between enemies and player
# Tiles
# Camera 

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

        self.obstacles = []

        ground = Obstacle(self.screen, self.ground_img, (0, 300))
        print(f"ground {ground.rect}")
        self.obstacles.append(ground)

        platform_img1 = pygame.Surface((200, 50))
        platform_img1.fill((255, 0, 0))
        platform1 = Obstacle(self.screen, platform_img1, (150, 200))
        self.obstacles.append(platform1)

        platform_img2 = pygame.Surface((200, 50))
        platform_img2.fill((255, 0, 0))
        platform2 = Obstacle(self.screen, platform_img2, (150, 50))
        self.obstacles.append(platform2)

        pipe1_img = pygame.Surface((50, 100))
        pipe1_img.fill((255, 0, 0))
        pipe1 = Obstacle(self.screen, pipe1_img, (400, 200))
        self.obstacles.append(pipe1)

        pipe2_img = pygame.Surface((50, 100))
        pipe2_img.fill((255, 0, 0))
        pipe2 = Obstacle(self.screen, pipe2_img, (700, 200))
        self.obstacles.append(pipe2)

        self.player = Player(self.player_images, self.screen, self.obstacles)
        self.enemies = []

        enemy = Enemy(self.screen, self.snail_images, self.obstacles + [self.player])
        self.enemies.append(enemy)

        self.player.obstacles.append(enemy)

    def run(self):
        clock = pygame.time.Clock()

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

            self.player.update()
            self.player.render()

            for obstacle in self.obstacles:
                obstacle.render()

            for enemy in self.enemies:
                enemy.update()
                enemy.render()

            pygame.display.update()

            clock.tick(Game.FPS)

game = Game()
game.run()

