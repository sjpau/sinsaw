import pygame
import mapper
from math import atan2, degrees

class GameObject:
    def __init__(self, pos, xy, image, is_tile):
        self.pos = pos
        self.image = pygame.transform.scale(image, (mapper.tile_size, mapper.tile_size))
        self.default_image = self.image
        self.direction = pygame.math.Vector2(1, 0)
        self.direction_ptr = self.direction.copy()
        if is_tile:
            self.rect = self.image.get_rect()
        else:
            self.rect = self.image.get_rect(topleft = xy)
    
    def on_tile_index(self, layout, tiles):
        return mapper.get_tile_index_from_layout(layout, tiles, self.pos)
    
    def on_tile_collides_with(self, collider, layout, tiles):
        if self.on_tile_index(layout, tiles) == collider.on_tile_index(layout, tiles):
            return True
        return False
    
def pos_in_layout_borders(pos, layout):
    MAX = len(layout)
    MIN = 0
    if pos[0] >= MIN and pos[0] < MAX and pos[1] >= 0 and pos[1] < MAX:
        return True

def update(self):
    if self.direction != self.direction_ptr:
        angle = degrees(atan2(self.direction[1], self.direction[0])) % 360
        self.image = pygame.transform.scale(pygame.transform.rotate(self.default_image, angle), (mapper.tile_size, mapper.tile_size))

class Weapon(pygame.sprite.Sprite, GameObject):
    def __init__(self, pos, xy, group):
        super().__init__(group)
        gameobject.GameObject.__init__(self, pos)