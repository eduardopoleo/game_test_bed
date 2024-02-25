# TODO:
# make the snail move to the left 
# Add jump and gravity

import pygame
import sys
import random

FPS = 60

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jumper Game")

# Background
ground_img = pygame.image.load('graphics/Ground.png').convert()
sky_img = pygame.image.load('graphics/Sky.png').convert()

# Player image
player_img = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# mid of the picture is at 80
# bottom of the pic  is at 300 
# this makes the calculations taking into account the image sizes.
player_rect = player_img.get_rect(midbottom=(80, 300))

# Snail
SNAIL_SPEED = 2
SPAWN_INTERVAL = 2 # spawn an enemy at every interval
snail_img = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

# Flies
OBSTACLE_SPEED = 2
fly_img = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacles = []

clock = pygame.time.Clock()

current_time = pygame.time.get_ticks() / 1000
initial_time = pygame.time.get_ticks() / 1000

class Obstacle:
    def __init__(self, img, screen, height):
        self.img = img
        self.screen = screen
        self.rect = img.get_rect(midbottom=(random.randint(800, 950), height))

    def update(self):
        self.rect.x -= OBSTACLE_SPEED

    def render(self):
        self.screen.blit(self.img, self.rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(sky_img, (0, 0))
    screen.blit(ground_img, (0, 300))
    # screen.blit(player_img, player_rect)

    current_time = pygame.time.get_ticks() / 1000
    time_elapsed = current_time - initial_time

    if time_elapsed >= SPAWN_INTERVAL:
        initial_time = current_time
        enemy_type = random.choice(['fly', 'snail'])
        new_obstacle = None
        if enemy_type == 'snail':
            new_obstacle = Obstacle(snail_img, screen, 300)
        else:
            new_obstacle = Obstacle(fly_img, screen, 200)
        
        obstacles.append(new_obstacle)

    for obstacle in obstacles:
        if obstacle.rect.x < -200:
            obstacles.remove(obstacle)
        else:
            obstacle.update()
            obstacle.render()
            
    print(len(obstacles))
    pygame.display.update()

    clock.tick(FPS)
