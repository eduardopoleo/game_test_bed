import pygame
import sys
import random
from objects.obstacle import Obstacle
from objects.player import Player

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

        self.obstacles = []
        self.player = Player(self.player_images, self.screen)

    def run(self):
        clock = pygame.time.Clock()

        current_time = pygame.time.get_ticks() / 1000
        initial_time = pygame.time.get_ticks() / 1000

        player = Player(self.player_images, self.screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.jumping = True
                    if event.key == pygame.K_RIGHT:
                        player.walking_forward = True
                    if event.key == pygame.K_LEFT:
                        player.walking_backwards = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.walking_forward = False
                    if event.key == pygame.K_LEFT:
                        player.walking_backwards = False

            self.screen.blit(self.sky_img, (0, 0))
            self.screen.blit(self.ground_img, (0, 300))

            current_time = pygame.time.get_ticks() / 1000
            time_elapsed = current_time - initial_time

            if time_elapsed >= Obstacle.SPAWN_INTERVAL:
                initial_time = current_time
                enemy_type = random.choice(['fly', 'snail'])
                new_obstacle = None
                if enemy_type == 'snail':
                    new_obstacle = Obstacle(self.screen, 300, self.snail_images)
                else:
                    new_obstacle = Obstacle(self.screen, 200, self.fly_images)

                self.obstacles.append(new_obstacle)

            player.update()
            player.render()

            obstacle_to_remove = None
            for obstacle in self.obstacles:
                if obstacle.rect.x < -200:
                    obstacle_to_remove = obstacle
                else:
                    obstacle.update()
                    # obstacle.render()

            if obstacle_to_remove:
                self.obstacles.remove(obstacle_to_remove)

            pygame.display.update()

            clock.tick(Game.FPS)
