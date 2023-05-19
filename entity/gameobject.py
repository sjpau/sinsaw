import pygame
import loader.asset as asset
import misc
from math import atan2, degrees

class GameObject:
    def __init__(self, pos, xy, image, is_tile):
        from loader.mapper import tile_size
        self.pos = pos
        self.image = pygame.transform.scale(image, (tile_size, tile_size))
        self.default_image = self.image
        self.direction = pygame.math.Vector2(1, 0)
        self.direction_ptr = self.direction.copy()
        if is_tile:
            self.rect = self.image.get_rect()
        else:
            self.rect = self.image.get_rect(topleft = xy)
    
    def on_tile_index(self, layout, tiles):   
        from loader.mapper import  get_tile_index_from_layout 
        return get_tile_index_from_layout(layout, tiles, self.pos)
    
    def on_tile_collides_with(self, collider, layout, tiles):
        if self.on_tile_index(layout, tiles) == collider.on_tile_index(layout, tiles):
            return True
        return False
    
    def on_shot(self):
        pass
    
    def shoot(self, layout, tiles, objects, weapon):
        from loader.mapper import pos_to_xy, get_tile_index_from_layout, status
        if weapon == 1: # Fire extinguisher
            extinguisher_slice = misc.molotow_slice(layout, self.pos, h_area=2, v_area=2)
            for tile_pos in extinguisher_slice:
                i = get_tile_index_from_layout(layout, tiles, tile_pos) # TODO split into separate functions
                if status['walkable'] in tiles[i].status or status['unlockable'] in tiles[i].status or status['breachable'] in tiles[i].status: 
                    tiles[i].affected = 2 # Set in fog
        elif weapon == 2: # Pistol
            tiles_content = misc.slice_from_direction(layout, self.direction, self.pos)
            for i, tile in enumerate(tiles_content):
                for game_obj in objects:
                    if game_obj.pos == [tile[0], tile[1]]:
                        game_obj.on_shot()
                if status['indestructable'] in tiles[get_tile_index_from_layout(layout, tiles, [tile[0], tile[1]])].status:
                    collide_pos = tiles_content[i]
                    break
        elif weapon == 4: # Molotow
            tiles_content = misc.slice_from_direction(layout, self.direction, self.pos)
            collide_pos = []
            for i, tile in enumerate(tiles_content):
                tmp_tile_stat = tiles[get_tile_index_from_layout(layout, tiles, [tile[0], tile[1]])].status
                if status['indestructable'] in tmp_tile_stat or status['destructable'] in tmp_tile_stat or status['breachable'] in tmp_tile_stat or status['unlockable'] in tmp_tile_stat:
                    collide_pos = tiles_content[i]
                    molotow_slice = misc.molotow_slice(layout, collide_pos)
                    for tile_pos in molotow_slice:
                        i = get_tile_index_from_layout(layout, tiles, tile_pos)
                        tiles[i].affected = 1 # Set on fire
                    break

    def update_object(self):
        if self.direction != self.direction_ptr:
            from loader.mapper import tile_size
            angle = degrees(atan2(self.direction[1], self.direction[0])) % 360
            self.image = pygame.transform.scale(pygame.transform.rotate(self.default_image, angle), (tile_size, tile_size))