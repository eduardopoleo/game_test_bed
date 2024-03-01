# TODO:
# make the snail move to the left 
# Add jump and gravity
# remap this cgn to something a bit easier 
# set list by default in neovim config

import pygame
import sys
import random
import math
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
    MAX_JUMP_HEIGTH = 100
    GRAVITY = 0.5
    WALKING_SPEED = 5
    WALKING_ANIMATION_TRANSITION = 0.05

    STAND             = 0
    WALKING_FORWARD_1 = 1
    WALKING_FORWARD_2 = 2
    JUMP              = 3

    def __init__(self, images):
        self.images = images
        self.jumping = False
        self.falling = False
        self.walking_forward = False
        self.walking_backwards = False
        self.walking_forward_img_idx = 1
        self.walking_backwards_img_idx = 0
        self.rect = images[Player.STAND].get_rect(midbottom=(80, Player.GROUND_ELEVATION))

    def update(self):
        if self.jumping:
            current_speed = math.sqrt(2 * Player.GRAVITY * (self.rect.bottom - Player.MAX_JUMP_HEIGTH))
            if current_speed == 0:
                self.jumping = False
                self.falling = True
                # To make things consistent the descent process is also dependent on the MAX_JUMP_HEIGTH
                # We need to kick off the descending process from here so that the substraction below
                # does not always stays at 0
                self.rect.bottom = Player.MAX_JUMP_HEIGTH + 1
                return

            self.rect.y -= current_speed

        if self.falling:
            current_speed = math.sqrt(2 * Player.GRAVITY * (self.rect.bottom - Player.MAX_JUMP_HEIGTH))
            self.rect.y += current_speed

            if self.rect.bottom >= Player.GROUND_ELEVATION:
                self.falling = False
                self.rect.bottom = Player.GROUND_ELEVATION

        if self.is_walking():
            self.rect.x += self.walking_direction() * Player.WALKING_SPEED

    def render(self):
        img_idx = None

        if self.jumping:
            img_idx = Player.JUMP
        elif self.is_walking():
            self.walking_forward_img_idx += Player.WALKING_ANIMATION_TRANSITION 
            if self.walking_forward_img_idx > Player.WALKING_FORWARD_2:
                self.walking_forward_img_idx = Player.WALKING_FORWARD_1
            img_idx = round(self.walking_forward_img_idx)
        else:
            img_idx = Player.STAND

        screen.blit(self.images[img_idx], self.rect)

    def walking_direction(self):
        return self.walking_forward - self.walking_backwards

    def is_walking(self):
        # the only ways this is true is if both walking_backwards and forward are
        # different 
        return self.walking_direction() != 0

player = Player(player_images)
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
            # obstacle.render()

    if obstacle_to_remove:
        obstacles.remove(obstacle_to_remove)

    pygame.display.update()

    clock.tick(FPS)
