import pygame

class Obstacle:
    def __init__(self, screen, image, coordinates):
        self.screen = screen
        self.image = image
        self.rect = image.get_rect(topleft=coordinates)
        self.old_rect = self.rect.copy()

    def render(self, offset):
        self.screen.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))

    def update(self):
        pass

