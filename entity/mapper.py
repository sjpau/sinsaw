import pygame
import camera
import asset
import gameobject

tile_size = 64

status_destructable = 0
status_indestructable = 1
status_walkable = 2
status_unwalkable = 3
status_transparent = 4

class Tile(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, group, image):
        super().__init__(group)
        pos = [0,0]
        gameobject.GameObject.__init__(self, pos, pos, image, True)
        self.code = -1
        self.status = []
    
    def init_status(self):
        if self.code == 0:
            self.status = [status_walkable, status_transparent]
        elif self.code == 1:
            self.status = [status_indestructable]
        elif self.code == 2:
            self.status = [status_destructable, status_walkable]


def init_tileset(layout, camera_group):
    tiles = []
    for y, row in enumerate(layout):
        for x, layout in enumerate(row):

            filename =  asset.static_path + asset.tileset[str(layout)] 
            image = pygame.image.load(filename).convert_alpha()
            image = pygame.transform.scale(image, (tile_size, tile_size))
            tile = Tile(camera_group, image)

            tile.rect.x = x * tile.rect.width
            tile.rect.y = y * tile.rect.height
            
            tile.code = layout
            tile.pos[0] = x
            tile.pos[1] = y

            tile.init_status()

            tiles.append(tile)
    
    return tiles

def get_tile_index_from_layout(layout, tiles, matrix_index):
    for row in range(len(layout)):
        for col in range(len(layout[row])): 
            if row == matrix_index[0] and col == matrix_index[1]:
                index = row * len(layout[row]) + col
    
    return index

def pos_to_xy(pos, layout, tiles):
    tile_index = get_tile_index_from_layout(layout, tiles, pos)
    xy = (tiles[tile_index].rect.x, tiles[tile_index].rect.y)
    return xy


def tileset_pixel_size(layout, tile_size):
    width = len(layout[0]) * tile_size
    height = len(layout) * tile_size
    return (width, height)