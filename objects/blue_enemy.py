
import random
from physics import *

class BlueEnemy:
    SPEED = 4

    def __init__(self, screen, image, coordinates):
        self.image = image
        self.obstacles = []
        self.player = None
        self.screen = screen
        self.direction = [1, 0]
        self.rect = self.image.get_rect(midbottom=coordinates)
        self.old_rect = self.rect.copy()
        self.vertical_velocity = 0
        self.dead = False
        self.spiky_top = True

    def update(self):
        self.old_rect = self.rect.copy()

        exert_gravity(self) 
        self.rect.x += self.direction[0] * BlueEnemy.SPEED

        if not self.dead:
            for obstacle in self.obstacles:
               collisions = calculate_collisions(self, obstacle)

               if collisions['right']:
                    self.direction[0] = -1

               if collisions['left']:
                    self.direction[0] = 1
               
    def render(self):
        self.screen.blit(self.image, self.rect)
