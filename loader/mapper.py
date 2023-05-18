import pygame
import loader.asset as asset
import entity.tile as tile

tile_size = 128

status = {
    'destructable': 0,
    'indestructable': 1,
    'walkable': 2,
    'transparent': 3,
    'unlockable': 4,
    'breachable': 5
}

def init_tileset(layout, camera_group):
    tiles = []
    for y, row in enumerate(layout):
        for x, layout in enumerate(row):

            filename =  asset.static_path + asset.tileset[str(layout)] 
            image = pygame.image.load(filename).convert_alpha()
            image = pygame.transform.scale(image, (tile_size, tile_size))
            t = tile.Tile(camera_group, image)

            t.rect.x = x * t.rect.width
            t.rect.y = y * t.rect.height
            
            t.code = layout
            t.pos[0] = x
            t.pos[1] = y

            t.init_status()

            tiles.append(t)
    
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

def pos_in_layout_borders(pos, layout):
    MAX = len(layout)
    MIN = 0
    if pos[0] >= MIN and pos[0] < MAX and pos[1] >= 0 and pos[1] < MAX:
        return True