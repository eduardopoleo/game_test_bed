import random

class Enemy:
    SPEED = 4
    SPAWN_INTERVAL = 2 # spawn an enemy at every interval
    ANIMATION_TRANSITION = 0.05

    def __init__(self, screen, height, images):
        self.images = images
        self.screen = screen
        self.rect = images[0].get_rect(midbottom=(random.randint(800, 950), height))
        self.current_img_idx = 0

    def update(self):
        self.rect.x -= Enemy.SPEED

    def render(self):
        self.current_img_idx = self.current_img_idx + Enemy.ANIMATION_TRANSITION
        if self.current_img_idx >= (len(self.images) - 1):
            self.current_img_idx = 0

        self.screen.blit(self.images[round(self.current_img_idx)], self.rect)


