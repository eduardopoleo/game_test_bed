import pygame

class Player:
    GROUND_ELEVATION = 300

    # velocity constants
    GRAVITY = 0.4
    WALKING_VELOCITY = 5
    JUMP_VELOCITY = -9 
    TERMINAL_VELOCITY = 20
    
    # sprite related constants
    STAND = 0
    WALKING_RIGHT_1 = 1
    WALKING_RIGHT_2 = 2
    JUMP = 3
    WALKING_ANIMATION_TRANSITION = 0.05

    def __init__(self, images, screen, obstacles):
        super().__init__()
        self.images = images
        self.screen = screen
        self.obstacles = obstacles
        self.direction = [0, 0]
        self.vertical_velocity = 0
        self.walking_forward_img_idx = 1
        self.image = images[Player.STAND]
        self.rect = images[Player.STAND].get_rect(midbottom=(80, Player.GROUND_ELEVATION))
        self.old_rect = self.rect.copy()
 
    def update(self):
        self.old_rect = self.rect.copy()

        self.rect.y += self.vertical_velocity
        self.vertical_velocity = self.vertical_velocity + Player.GRAVITY
        self.rect.x += self.direction[0] * self.WALKING_VELOCITY

        self.check_collisions('horizontal')
        self.check_collisions('vertical')

    def check_collisions(self, direction):
        for obstacle in self.obstacles:
            if self.rect.colliderect(obstacle):
                if direction == 'horizontal':
                    if self.rect.right >= obstacle.rect.left and self.old_rect.right <= obstacle.old_rect.left: 
                        self.rect.right = obstacle.rect.left
                    elif self.rect.left <= obstacle.rect.right and self.old_rect.left >= obstacle.old_rect.right:
                        self.rect.left = obstacle.rect.right
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
        img_idx = None

        if self.moving_vertically():
            img_idx = Player.JUMP
        elif self.moving_horizontally():
            self.walking_forward_img_idx += Player.WALKING_ANIMATION_TRANSITION 
            if self.walking_forward_img_idx > Player.WALKING_RIGHT_2:
                self.walking_forward_img_idx = Player.WALKING_RIGHT_1
            img_idx = round(self.walking_forward_img_idx)
        else:
            img_idx = Player.STAND

        self.image = self.images[img_idx]

        self.screen.blit(self.image, (self.rect.x, self.rect.y))


    def start_jump(self):
        self.vertical_velocity = Player.JUMP_VELOCITY
        self.direction[1] = -1

    def moving_horizontally(self):
        return self.direction[0] != 0

    def moving_vertically(self):
        return self.direction[1] != 0
