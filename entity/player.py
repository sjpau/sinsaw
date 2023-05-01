import pygame
import mapper
import gameobject

class Player(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group):
        super().__init__(group)
        gameobject.GameObject.__init__(self, pos)
        image = pygame.image.load("asset/player.jpg").convert_alpha()
        self.image = pygame.transform.scale(image, (mapper.tile_size, mapper.tile_size))
        self.rect = self.image.get_rect(topleft = xy)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 1
    
    def move_down(self, layout, tiles):
        self.direction.y = 1
        self.direction.x = 0
        if gameobject.pos_in_layout_borders([self.pos[0] + 1, self.pos[1]], layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, [self.pos[0] + 1, self.pos[1]])]
            for status in next_tile.status:
                if status == mapper.status_walkable:
                    self.pos[0] += 1

    def move_up(self, layout, tiles):
        self.direction.y = -1
        self.direction.x = 0
        if gameobject.pos_in_layout_borders([self.pos[0] - 1, self.pos[1]], layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, [self.pos[0] - 1, self.pos[1]])]
            for status in next_tile.status:
                if status == mapper.status_walkable:
                    self.pos[0] -= 1

    def move_left(self, layout, tiles):
        self.direction.x = -1
        self.direction.y = 0
        if gameobject.pos_in_layout_borders([self.pos[0], self.pos[1] - 1], layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, [self.pos[0], self.pos[1] - 1])]
            for status in next_tile.status:
                if status == mapper.status_walkable:
                    self.pos[1] -= 1

    def move_right(self, layout, tiles):
        self.direction.x = 1
        self.direction.y = 0
        if gameobject.pos_in_layout_borders([self.pos[0], self.pos[1] + 1], layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, [self.pos[0], self.pos[1] + 1])]
            for status in next_tile.status:
                if status == mapper.status_walkable:
                    self.pos[1] += 1

  
    def update(self, layout, tiles):

        xy = mapper.pos_to_xy(self.pos, layout, tiles)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

        if self.on_tile_collides_with([15,15], layout, tiles):
            print('collision!')
       