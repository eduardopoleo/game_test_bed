# TODO:
# make the snail move to the left 
# Add jump and gravity

import pygame
import sys
import random
from objects.obstacle import Obstacle
FPS = 60

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jumper Game")

# Background
ground_img = pygame.image.load('graphics/Ground.png').convert()
sky_img = pygame.image.load('graphics/Sky.png').convert()

player_images = [
    pygame.image.load('graphics/Player/player_stand.png').convert_alpha(),
    pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(),
    pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha(),
    pygame.image.load('graphics/Player/jump.png').convert_alpha()
]

snail_images = [
    pygame.image.load('graphics/snail/snail1.png').convert_alpha(),
    pygame.image.load('graphics/snail/snail2.png').convert_alpha()
]

fly_images = [
    pygame.image.load('graphics/Fly/Fly1.png').convert_alpha(),
    pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
]

obstacles = []

clock = pygame.time.Clock()

current_time = pygame.time.get_ticks() / 1000
initial_time = pygame.time.get_ticks() / 1000

class Player:
    GROUND_ELEVATION = 300
    MAX_JUMP_HEIGTH = 50
    INITIAL_FALL_SPEED = 1
    GRAVITY = 0.2 

    STAND     = 0
    WALKING_1 = 1
    WALKING_2 = 2
    JUMP      = 3

    def __init__(self, images):
        self.images = images
        self.jumping = False
        self.rect = images[Player.STAND].get_rect(midbottom=(80, Player.GROUND_ELEVATION))
        self.fall_speed = Player.INITIAL_FALL_SPEED
 
    def update(self):
        if self.jumping:
            self.rect.y += self.fall_speed
            self.fall_speed += Player.GRAVITY

        if self.rect.bottom >= Player.GROUND_ELEVATION:
            self.jumping = False
            self.rect.bottom = Player.GROUND_ELEVATION
            self.fall_speed = Player.INITIAL_FALL_SPEED 

    def render(self):
        img = Player.JUMP if player.jumping else Player.STAND
        screen.blit(self.images[img], self.rect)

player = Player(player_images)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.rect.y = Player.MAX_JUMP_HEIGTH
                player.jumping = True

    screen.blit(sky_img, (0, 0))
    screen.blit(ground_img, (0, 300))

    current_time = pygame.time.get_ticks() / 1000
    time_elapsed = current_time - initial_time

    if time_elapsed >= Obstacle.SPAWN_INTERVAL:
        initial_time = current_time
        enemy_type = random.choice(['fly', 'snail'])
        new_obstacle = None
        if enemy_type == 'snail':
            new_obstacle = Obstacle(screen, 300, snail_images)
        else:
            new_obstacle = Obstacle(screen, 200, fly_images)
        
        obstacles.append(new_obstacle)

    player.update()
    player.render()

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
