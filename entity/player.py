import pygame
import entity.gameobject as gameobject
import loader.asset as asset
import entity.item as item
import loader.mapper as mapper

class Player(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group, attached_item=None):
        super().__init__(group)
        init_image = pygame.image.load(asset.image_player_gun).convert_alpha()
        gameobject.GameObject.__init__(self, pos, xy, init_image, False)
        self.attached_item = None
        self.alive = True
    
    def die(self):
        # Write when die state
        self.alive = False
    
    def on_shot(self):
        super().on_shot()
        self.die()

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
                        next_tile.status.remove(mapper.status['unlockable'])
                        next_tile.status.append(mapper.status['breachable'])
                        self.attached_item = None

    def update(self, layout, tiles, items=None):

        if tiles[mapper.get_tile_index_from_layout(layout, tiles, self.pos)].affected == 1:
            self.die()
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
                    else:
                        self.attached_item.discarded = True
                        self.attach_item(i)
                        i.play_sfx_pick()
                        i.dropped = False
        xy = mapper.pos_to_xy(self.pos, layout, tiles)
        self.rect.x = xy[0]
        self.rect.y = xy[1]
        self.update_object()