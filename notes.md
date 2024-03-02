# We can create groups to check collisions on using the sprite class
```python
# every single sprite
all_sprites = pygame.sprite.Group()
# every single sprite the player will collide with (obstacles and enemies)
collision_sprite = pygame.sprite.Group()

# when creating the class we make it inherit from the sprite class

class Something(pygagme.sprite.Sprite):
    def __init__(self):
        # The groups the sprite will be in
        super().__init__(groups)

# to check on collision
pygame.sprite.spritecollide(sprite, group, dokill)
# the specific sprite we're checking on 
# the group we're checking agaist
# if we remove the element that collided from the group


# we can them do to update them and to draw them
all_sprites.update(dt) # not sure if I can pass the frame rate in here
all_sprites.draw(screen)


# tolA more eaiser create rectangles we
# create an image
img = pygame.Surface((width, height))
# add color to it
img.fill('blue')
# position it using the get_rect coordinates
image.get_rect(topleft=(640, 360))
```
