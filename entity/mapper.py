import pygame
import camera

tile_size = 64

tileset = {
    "0": "floor_1.png",
    "1": "wall_1.png",
    "2": "door_1.png"
}

class Tile(pygame.sprite.Sprite):
    def __init__(self, group, image):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()

def init_tileset(layout, camera_group):
    tiles = []
    for y, row in enumerate(layout):
        for x, layout in enumerate(row):

            filename = "asset/static/" + tileset[str(layout)] 
            image = pygame.image.load(filename).convert_alpha()
            image = pygame.transform.scale(image, (tile_size, tile_size))
            tile = Tile(camera_group, image)

            tile.rect.x = x * tile.rect.width
            tile.rect.y = y * tile.rect.height

            tiles.append(tile)
    
    return tiles

def get_tile_index_from_layout(layout, tiles, matrix_index):
    for row in range(len(layout)):
        for col in range(len(layout[row])): 
            if row == matrix_index[0] and col == matrix_index[1]:
                index = row * len(layout[row]) + col
    return index


def tileset_pixel_size(layout, tile_size):
    width = len(layout[0]) * tile_size
    height = len(layout) * tile_size
    return (width, height)