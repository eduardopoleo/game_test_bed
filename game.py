# TODO:
# Remove the usage of silly sprites and make everything lists
# Remove the pictures and make eveything based on blocks
# Calculate the collissions between enemies and player
# Tiles
# Camera 

import pygame
import sys
import random
from objects.green_enemy import GreenEnemy
from objects.blue_enemy import BlueEnemy
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

        self.enemies = []

        self.obstacles = []

        ground_img = pygame.Surface((10000, 400))
        ground_img.fill((110, 38, 14))
        ground = Obstacle(self.screen, ground_img, (0, 300))
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

        pipe3_img = pygame.Surface((50, 100))
        pipe3_img.fill((255, 0, 0))
        pipe3 = Obstacle(self.screen, pipe2_img, (1000, 200))
        self.obstacles.append(pipe3)

        blue_enemy_img = pygame.Surface((50, 50))
        blue_enemy_img.fill((0, 0, 255))
        blue_enemy = BlueEnemy(self.screen, blue_enemy_img, (800, 200))
        blue_enemy.obstacles = self.obstacles

        green_img = pygame.Surface((50, 50))
        green_img.fill((0, 255, 0))
        green_enemy = GreenEnemy(self.screen, green_img, (600, 200))
        green_enemy.obstacles = self.obstacles

        self.enemies = []
        self.enemies = [green_enemy, blue_enemy]
        
        player_img = pygame.Surface((60, 80))
        player_img.fill((218, 160, 109))
        self.player = Player(player_img, self.screen) 
        self.player.enemies = self.enemies
        self.player.obstacles = self.obstacles

        blue_enemy.player = self.player
        green_enemy.player = self.player

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

            self.screen.fill((0,0,0))

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

