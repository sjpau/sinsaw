import pygame
import random
import defs.finals as finals
import entity.gameobject as gameobject
from entity.animation import Animation
import loader.asset as asset
import entity.item as item
import loader.mapper as mapper
import loader.anims as anims
import entity.particles as particles

class Player(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group, attached_item=None):
        super().__init__(group)
        self.group = group
        anim_default_attack, anim_default_idle, anim_default_smoking, anim_default_walk = anims.load_animations_player_default()
        anim_molotow_attack, anim_molotow_idle,  anim_molotow_walk = anims.load_animations_player_molotow()
        anim_exting_idle,  anim_exting_walk = anims.load_animations_player_exting()
        anim_knife_attack, anim_knife_idle,  anim_knife_walk = anims.load_animations_player_knife()
        anim_gun_attack, anim_gun_idle,  anim_gun_walk = anims.load_animations_player_gun()
        animations_player = {
            'default_attack': Animation(anim_default_attack, 50),
            'default_idle': Animation(anim_default_idle, 100),
            'default_smoking': Animation(anim_default_smoking, 100),
            'molotow_attack': Animation(anim_molotow_attack, 50),
            'molotow_idle': Animation(anim_molotow_idle, 100),
            'molotow_walk': Animation(anim_molotow_walk, 100),
            'exting_idle': Animation(anim_exting_idle, 100),
            'exting_walk': Animation(anim_exting_idle, 100),
            'knife_attack': Animation(anim_knife_attack, 50),
            'knife_idle': Animation(anim_knife_idle, 100),
            'knife_walk': Animation(anim_knife_walk, 100),
            'gun_attack': Animation(anim_gun_attack, 50),
            'gun_idle': Animation(anim_gun_idle, 100),
            'gun_walk': Animation(anim_gun_idle, 100),
        }
        self.animations = animations_player 
        init_image = pygame.image.load(asset.image_player_gun).convert_alpha()
        gameobject.GameObject.__init__(self, pos, xy, init_image, False,group, animations=self.animations)
        self.attached_item = None
        self.alive = True
    
    def die(self, particles_list):
        # Write when die state
        for i in range(30):
            particles_list.append(particles.Particle(self.rect.bottomright, finals.COLOR_RED, random.randint(1, 2), finals.COLOR_RED, velocity=pygame.Vector2(random.uniform(random.randint(-20, 0), random.randint(0, 20)), random.uniform(random.randint(-20, 0), random.randint(0, 20))), tag=1))
        self.alive = False
    
    def on_shot(self, particles_list):
        super().on_shot(particles_list)
        for i in range(50):
            particles_list.append(particles.Particle(self.rect.bottomright, finals.COLOR_RED, random.randint(1, 2), finals.COLOR_RED, velocity=pygame.Vector2(random.uniform(-20, 10), random.uniform(-10, 10)), tag=1))
        self.die(particles_list)

    def attach_item(self, attached_item):
        self.attached_item = attached_item
 
    def move_down(self, layout, tiles):
        self.direction_ptr = self.direction.copy()
        self.direction.x = 0
        self.direction.y = -1
        next_pos = [self.pos[0] + 1, self.pos[1]]
        if mapper.pos_in_layout_borders(next_pos, layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, next_pos)]
            for status in next_tile.status:
                if status == mapper.status['walkable'] or status == mapper.status['breachable']:
                    self.pos[0] += 1
                if self.attached_item is not None:
                    if status == mapper.status['unlockable'] and self.attached_item.category == 5 : # Unlockable door and has key
                        next_tile.change_image()
                        next_tile.status.remove(mapper.status['unlockable'])
                        next_tile.status.append(mapper.status['breachable'])
                        self.attached_item = None

    def move_up(self, layout, tiles):
        self.direction_ptr = self.direction.copy()
        self.direction.x = 0
        self.direction.y = 1
        next_pos = [self.pos[0] - 1, self.pos[1]]
        if mapper.pos_in_layout_borders(next_pos, layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, next_pos)]
            for status in next_tile.status:
                if status == mapper.status['walkable'] or status == mapper.status['breachable']:
                    self.pos[0] -= 1
                if self.attached_item is not None:
                    if status == mapper.status['unlockable'] and self.attached_item.category == 5 : # Unlockable door and has key
                        next_tile.change_image()
                        next_tile.status.remove(mapper.status['unlockable'])
                        next_tile.status.append(mapper.status['breachable'])
                        self.attached_item = None

    def move_left(self, layout, tiles):
        self.direction_ptr = self.direction.copy()
        self.direction.x = -1
        self.direction.y = 0
        next_pos = [self.pos[0], self.pos[1] - 1]
        if mapper.pos_in_layout_borders(next_pos, layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, next_pos)]
            for status in next_tile.status:
                if status == mapper.status['walkable'] or status == mapper.status['breachable']:
                    self.pos[1] -= 1
                if self.attached_item is not None:
                    if status == mapper.status['unlockable'] and self.attached_item.category == 5 : # Unlockable door and has key
                        next_tile.change_image()
                        next_tile.status.remove(mapper.status['unlockable'])
                        next_tile.status.append(mapper.status['breachable'])
                        self.attached_item = None

    def move_right(self, layout, tiles):
        self.direction_ptr = self.direction.copy()
        self.direction.x = 1
        self.direction.y = 0
        next_pos = [self.pos[0], self.pos[1] + 1]
        if mapper.pos_in_layout_borders(next_pos, layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, next_pos)]
            for status in next_tile.status:
                if status == mapper.status['walkable'] or status == mapper.status['breachable']:
                    self.pos[1] += 1
                if self.attached_item is not None:
                    if status == mapper.status['unlockable'] and self.attached_item.category == 5 : # Unlockable door and has key
                        next_tile.change_image()
                        next_tile.status.remove(mapper.status['unlockable'])
                        next_tile.status.append(mapper.status['breachable'])
                        self.attached_item = None

    def update(self, layout, tiles, items=None):
        if items is None:
            items = []
        else:
            for i in items:
                if self.on_tile_collides_with(i, layout, tiles):
                    if self.attached_item is None:
                        self.attach_item(i)
                        i.play_sfx_pick()
                        i.dropped = False
                        i.discarded = False
                        items.remove(i)
                        self.group.remove(i)
                    else:
                        self.attached_item.discarded = True
                        self.attach_item(i)
                        i.play_sfx_pick()
                        i.dropped = False
                        items.remove(i)
                        self.group.remove(i)
        xy = mapper.pos_to_xy(self.pos, layout, tiles)
        self.rect.x = xy[0]
        self.rect.y = xy[1]