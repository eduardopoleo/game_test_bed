import pygame
import sys

FPS = 60

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jumper Game")

ground_img = pygame.image.load('graphics/Ground.png').convert()
sky_img = pygame.image.load('graphics/Sky.png').convert()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(sky_img, (0, 0))
    screen.blit(ground_img, (0, 300))
    pygame.display.update()

    clock.tick(FPS)
