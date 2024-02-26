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
OBTACLE_ANIMATION_TRANSITION = 0.05
snail_images = [
    pygame.image.load('graphics/snail/snail1.png').convert_alpha(),
    pygame.image.load('graphics/snail/snail2.png').convert_alpha()
]

# Flies
OBSTACLE_SPEED = 2
fly_images = [
    pygame.image.load('graphics/Fly/Fly1.png').convert_alpha(),
    pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
]

obstacles = []

clock = pygame.time.Clock()

current_time = pygame.time.get_ticks() / 1000
initial_time = pygame.time.get_ticks() / 1000

class Obstacle:
    def __init__(self, screen, height, images):
        self.images = images
        self.screen = screen
        self.rect = images[0].get_rect(midbottom=(random.randint(800, 950), height))
        self.current_img_idx = 0

    def update(self):
        self.rect.x -= OBSTACLE_SPEED

    def render(self):
        self.current_img_idx = self.current_img_idx + OBTACLE_ANIMATION_TRANSITION
        if self.current_img_idx >= (len(self.images) - 1):
            self.current_img_idx = 0

        self.screen.blit(self.images[round(self.current_img_idx)], self.rect)

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
            new_obstacle = Obstacle(screen, 300, snail_images)
        else:
            new_obstacle = Obstacle(screen, 200, fly_images)
        
        obstacles.append(new_obstacle)

    obstacle_to_remove = None
    for obstacle in obstacles:
        if obstacle.rect.x < -200:
            obstacle_to_remove = obstacle
        else:
            obstacle.update()
            obstacle.render()
    
    if obstacle_to_remove:
        obstacles.remove(obstacle_to_remove) 
            
    pygame.display.update()

    clock.tick(FPS)
