from physics import *

class GreenEnemy:
    SPEED = 4
    ANIMATION_TRANSITION = 0.05

    def __init__(self, screen, image, coordinates):
        self.image = image
        self.obstacles = []
        self.player = None
        self.screen = screen
        self.direction = [1, 0]
        self.rect = self.image.get_rect(midbottom=coordinates)
        self.old_rect = self.rect.copy()
        self.current_img_idx = 0
        self.vertical_velocity = 0
        self.dead = False
        self.spiky_top = False

    def update(self):
        self.old_rect = self.rect.copy()

        exert_gravity(self) 
        self.rect.x += self.direction[0] * GreenEnemy.SPEED

        if not self.dead:
            for obstacle in self.obstacles:
               collisions = calculate_collisions(self, obstacle)

               if collisions['right']:
                    self.direction[0] = -1

               if collisions['left']:
                    self.direction[0] = 1
                
            if self.rect.colliderect(self.player) and top_collides(self, self.player):
                self.dead = True
    
    def render(self):
        self.screen.blit(self.image, self.rect)


