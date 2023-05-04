import pygame
import mapper

class GameObject:
    def __init__(self, pos):
        self.pos = pos
    
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