import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, image, coordinates):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = image.get_rect(topleft=coordinates)
        self.old_rect = self.rect.copy()

