import math

class Player:
    GROUND_ELEVATION = 300
    MAX_JUMP_HEIGTH = 100
    GRAVITY = 0.5
    WALKING_SPEED = 5
    WALKING_ANIMATION_TRANSITION = 0.05

    STAND             = 0
    WALKING_FORWARD_1 = 1
    WALKING_FORWARD_2 = 2
    JUMP              = 3

    def __init__(self, images, screen):
        self.images = images
        self.jumping = False
        self.falling = False
        self.screen = screen
        self.walking_forward = False
        self.walking_backwards = False
        self.walking_forward_img_idx = 1
        self.walking_backwards_img_idx = 0
        self.rect = images[Player.STAND].get_rect(midbottom=(80, Player.GROUND_ELEVATION))

    def update(self):
        if self.jumping:
            current_speed = math.sqrt(2 * Player.GRAVITY * (self.rect.bottom - Player.MAX_JUMP_HEIGTH))
            if current_speed == 0:
                self.jumping = False
                self.falling = True
                # To make things consistent the descent process is also dependent on the MAX_JUMP_HEIGTH
                # We need to kick off the descending process from here so that the substraction below
                # does not always stays at 0
                self.rect.bottom = Player.MAX_JUMP_HEIGTH + 1
                return

            self.rect.y -= current_speed

        if self.falling:
            current_speed = math.sqrt(2 * Player.GRAVITY * (self.rect.bottom - Player.MAX_JUMP_HEIGTH))
            self.rect.y += current_speed

            if self.rect.bottom >= Player.GROUND_ELEVATION:
                self.falling = False
                self.rect.bottom = Player.GROUND_ELEVATION

        if self.is_walking():
            self.rect.x += self.walking_direction() * Player.WALKING_SPEED

    def render(self):
        img_idx = None

        if self.jumping or self.falling:
            img_idx = Player.JUMP
        elif self.is_walking():
            # TODO: create sprite for walking walking and add it in here
            self.walking_forward_img_idx += Player.WALKING_ANIMATION_TRANSITION 
            if self.walking_forward_img_idx > Player.WALKING_FORWARD_2:
                self.walking_forward_img_idx = Player.WALKING_FORWARD_1
            img_idx = round(self.walking_forward_img_idx)
        else:
            img_idx = Player.STAND

        self.screen.blit(self.images[img_idx], self.rect)

    def walking_direction(self):
        return self.walking_forward - self.walking_backwards

    def is_walking(self):
        # the only ways this is true is if both walking_backwards and forward are
        # different 
        return self.walking_direction() != 0

