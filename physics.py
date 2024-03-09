def calculate_collisions(object1, object2):
    collisions = { 'top': False, 'bottom': False, 'left': False, 'right': False }
    if object1.rect.colliderect(object2):
        if object1.rect.colliderect(object2):
            if right_collides(object1, object2):
                collisions['right'] = True
                object1.rect.right = object2.rect.left
            elif left_collides(object1, object2):
                object1.rect.left = object2.rect.right
                collisions['left'] = True
            if top_collides(object1, object2):
                object1.rect.top = object2.rect.bottom
                object1.direction[1] = 1
                object1.vertical_velocity = 0
                collisions['top'] = True
            elif bottom_collides(object1, object2):
                object1.rect.bottom = object2.rect.top
                object1.direction[1] = 0
                object1.vertical_velocity = 0
                collisions['bottom'] = True
    return collisions

def right_collides(object1, object2):
    currently_intersects = object1.rect.right >= object2.rect.left 
    did_not_intersect = object1.old_rect.right <= object2.old_rect.left
    return currently_intersects and did_not_intersect

def left_collides(object1, object2):
    currently_intersects = object1.rect.left <= object2.rect.right 
    did_not_intersect = object1.old_rect.left >= object2.old_rect.right
    return currently_intersects and did_not_intersect

def top_collides(object1, object2):
    currently_intersects = object1.rect.top <= object2.rect.bottom 
    did_not_intersect = object1.old_rect.top >= object2.old_rect.bottom
    return currently_intersects and did_not_intersect

def bottom_collides(object1, object2):
    currently_intersects = object1.rect.bottom >= object2.rect.top 
    did_not_intersect = object1.old_rect.bottom <= object2.old_rect.top
    return currently_intersects and did_not_intersect

GRAVITY = 0.4 

def exert_gravity(object):
    object.rect.y += object.vertical_velocity
    object.vertical_velocity = object.vertical_velocity + GRAVITY
 
