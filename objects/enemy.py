import random

class Enemy:
    SPEED = 4
    GRAVITY = 0.4
    SPAWN_INTERVAL = 2 # spawn an enemy at every interval
    ANIMATION_TRANSITION = 0.05

    def __init__(self, screen, images, obstacles):
        self.images = images
        self.obstacles = obstacles
        self.screen = screen
        self.direction = [1, 0]
        self.rect = images[0].get_rect(midbottom=(500, 300))
        self.old_rect = self.rect.copy()
        self.current_img_idx = 0
        self.vertical_velocity = 0

    def update(self):
        self.old_rect = self.rect.copy()

        self.rect.y += self.vertical_velocity
        self.vertical_velocity = self.vertical_velocity + Enemy.GRAVITY
        self.rect.x += self.direction[0] * self.SPEED

        self.check_collisions('horizontal')
        self.check_collisions('vertical')

    def check_collisions(self, direction):
        for obstacle in self.obstacles:
            if self.rect.colliderect(obstacle):
                if direction == 'horizontal':
                    if self.rect.right >= obstacle.rect.left and self.old_rect.right <= obstacle.old_rect.left: 
                        self.rect.right = obstacle.rect.left
                        self.direction[0] = -1
                    elif self.rect.left <= obstacle.rect.right and self.old_rect.left >= obstacle.old_rect.right:
                        self.rect.left = obstacle.rect.right
                        self.direction[0] = 1
                if direction == 'vertical':
                    if self.rect.top <= obstacle.rect.bottom and self.old_rect.top >= obstacle.old_rect.bottom:
                        self.rect.top = obstacle.rect.bottom
                        self.direction[1] = 1
                        self.vertical_velocity = 0
                    elif self.rect.bottom >= obstacle.rect.top and self.old_rect.bottom <= obstacle.old_rect.top:
                        self.rect.bottom = obstacle.rect.top
                        self.direction[1] = 0
                        self.vertical_velocity = 0 

    def render(self):
        self.current_img_idx = self.current_img_idx + Enemy.ANIMATION_TRANSITION
        if self.current_img_idx >= (len(self.images) - 1):
            self.current_img_idx = 0

        self.screen.blit(self.images[round(self.current_img_idx)], self.rect)


