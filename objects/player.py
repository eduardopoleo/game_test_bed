import pygame
from physics import *

class Player:
    GROUND_ELEVATION = 300

    WALKING_VELOCITY = 5
    JUMP_VELOCITY = -9 
    TERMINAL_VELOCITY = 20
    
    # sprite related constants
    STAND = 0
    WALKING_RIGHT_1 = 1
    WALKING_RIGHT_2 = 2
    JUMP = 3
    WALKING_ANIMATION_TRANSITION = 0.05
    INVISIBILITY_FRAME_TRANSITION = 0.2 
    INVISIBILITY_DURATION = 1500

    def __init__(self, image, screen):
        self.screen = screen
        self.enemies = []
        self.obstacles = []
        self.vertical_velocity = 0
        self.walking_forward_img_idx = 1
        self.invincibility_frame_state = 0
        self.invincibility_start_time = 0
        self.image = image
        self.direction = [0, 0]
        self.rect = image.get_rect(midbottom=(80, Player.GROUND_ELEVATION))
        self.old_rect = self.rect.copy()
        self.invincible = False
 
    def update(self):
        self.old_rect = self.rect.copy()

        exert_gravity(self)

        self.rect.x += self.direction[0] * self.WALKING_VELOCITY

        self.check_collisions()

        current_time = pygame.time.get_ticks()
        if self.invincible and ((current_time - self.invincibility_start_time) > Player.INVISIBILITY_DURATION):
            self.invincible = False

    def check_collisions(self):
        for obstacle in self.obstacles:
            calculate_collisions(self, obstacle)
        
        if not self.invincible:
            for enemy in self.enemies:
                if self.rect.colliderect(enemy.rect):
                    if right_collides(self, enemy) or left_collides(self, enemy):
                        self.invincibility_start_time = pygame.time.get_ticks()
                        self.invincible = True
                    if enemy.spiky_top and bottom_collides(self, enemy):
                        self.invincibility_start_time = pygame.time.get_ticks()
                        self.invincible = True
 
    def render(self, offset):
        if self.invincible:
            self.invincibility_frame_state += Player.INVISIBILITY_FRAME_TRANSITION
            if  self.invincibility_frame_state >= 1:
                self.invincibility_frame_state = 0
                self.screen.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))
        else:
            self.screen.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))

    def start_jump(self):
        self.vertical_velocity = Player.JUMP_VELOCITY
        self.direction[1] = -1

    def moving_horizontally(self):
        return self.direction[0] != 0

    def moving_vertically(self):
        return self.direction[1] != 0
