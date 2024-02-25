import pygame
import sys

FPS = 60

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jumper Game")

# Background
ground_img = pygame.image.load('graphics/Ground.png').convert()
sky_img = pygame.image.load('graphics/Sky.png').convert()

# Player image
player_img = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_rect = player_img.get_rect(x=40, y=216)

# Snail image
snail_img = pygame.image.load('graphics/snail/snail1.png')
snail_rect = player_img.get_rect(x=700, y=264)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(sky_img, (0, 0))
    screen.blit(ground_img, (0, 300))
    screen.blit(player_img, player_rect)
    screen.blit(snail_img, snail_rect)

    pygame.display.update()

    clock.tick(FPS)
