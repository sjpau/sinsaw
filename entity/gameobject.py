import pygame
import mapper
import asset
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
    
    def on_shot(self):
        print('shot')
        pass
    
    def shoot(self, layout, tiles, objects):
        rows, cols = len(layout), len(layout[0])
        tiles_content = []
        x = self.pos[1]
        y = self.pos[0]
    # Keep moving in the specified direction until we reach the end of the matrix
        while 0 <= y < rows and 0 <= x < cols:
            tiles_content.append([[y,x],layout[y][x]])
            y -= int(self.direction.y)
            x += int(self.direction.x)
        tiles_content.pop(0)
        # Determine final collision point (indestructable tile)
        collide_pos = []
        print(objects)
        for i, tile in enumerate(tiles_content):
            for game_obj in objects:
                if game_obj.pos == [tile[0][0], tile[0][1]]:
                    game_obj.on_shot()
            if mapper.status_indestructable in tiles[mapper.get_tile_index_from_layout(layout, tiles, [tile[0][0], tile[0][1]])].status:
                collide_pos = tiles_content[i]
                break

def pos_in_layout_borders(pos, layout):
    MAX = len(layout)
    MIN = 0
    if pos[0] >= MIN and pos[0] < MAX and pos[1] >= 0 and pos[1] < MAX:
        return True


def update(self):
    if self.direction != self.direction_ptr:
        angle = degrees(atan2(self.direction[1], self.direction[0])) % 360
        self.image = pygame.transform.scale(pygame.transform.rotate(self.default_image, angle), (mapper.tile_size, mapper.tile_size))