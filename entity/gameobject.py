import pygame
import loader.asset as asset
import helper.misc as misc
from math import atan2, degrees
import loader.mapper as mapper
import defs.finals as finals

class GameObject:
    def __init__(self, pos, xy, image, is_tile, group, animations=None):
        self.animations = animations or {}
        self.current_animation = None
        self.pos = pos
        self.image = pygame.transform.scale(image, (finals.tile_size, finals.tile_size))
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
    
    def on_shot(self, particles_list):
        pass
    
    def shoot(self, layout, tiles, objects, weapon, particles_list):
        from loader.mapper import pos_to_xy, get_tile_index_from_layout, status
        if weapon == 1: # Fire extinguisher
            extinguisher_slice = misc.molotow_slice(layout, self.pos, h_area=2, v_area=2)
            for tile_pos in extinguisher_slice:
                i = get_tile_index_from_layout(layout, tiles, tile_pos) # TODO split into separate functions
                if status['walkable'] in tiles[i].status or status['unlockable'] in tiles[i].status or status['breachable'] in tiles[i].status: 
                    tiles[i].affected = 2 # Set in fog
                    if status['transparent'] in tiles[i].status:
                        tiles[i].status.remove(status['transparent'])
                        tiles[i].status.append(status['opaque'])
        elif weapon == 2: # Pistol
            tiles_content = misc.slice_from_direction(layout, self.direction, self.pos)
            for i, tile in enumerate(tiles_content):
                tiles[get_tile_index_from_layout(layout, tiles, tile)].on_shot(particles_list)
                for game_obj in objects:
                    if game_obj.pos == [tile[0], tile[1]]:
                        game_obj.on_shot(particles_list)
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
    
    def play(self, animation_name):
        if animation_name in self.animations:
            self.current_animation = self.animations[animation_name]
            self.default_image = self.current_animation.get_sprite(0)

    def is_object_visible(self, target, layout, tiles):
        object_y = self.pos[0]
        object_x = self.pos[1]
        target_y = target.pos[0]
        target_x = target.pos[1]
        dx = abs(target_x - object_x)
        dy = abs(target_y - object_y)
        sx = -1 if object_x > target_x else 1
        sy = -1 if object_y > target_y else 1
        err = dx - dy

        while object_x != target_x or object_y != target_y:
            if object_y < 0 or object_y >= len(layout) or object_x < 0 or object_x >= len(layout[0]):
                return False
            
            if mapper.status['transparent'] not in tiles[mapper.get_tile_index_from_layout(layout, tiles, [object_y, object_x])].status:
                return False

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                object_x += sx
            if e2 < dx:
                err += dx
                object_y += sy
        
        return True


    def update_object(self, dt):
        if self.current_animation is not None:
            self.current_animation.play(dt)
            angle = degrees(atan2(self.direction[1], self.direction[0])) % 360
            self.image = pygame.transform.scale(pygame.transform.rotate(self.current_animation.get_current_sprite(), angle), (finals.tile_size, finals.tile_size))