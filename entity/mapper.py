import pygame
import camera

tile_size = 32

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

def init(layout, camera_group):
    for y, row in enumerate(layout):
        for x, layout in enumerate(row):

            filename = "asset/static/" + tileset[str(layout)] 
            image = pygame.image.load(filename).convert_alpha()
            tile = Tile(camera_group, image)

            tile.rect.x = x * tile.rect.width
            tile.rect.y = y * tile.rect.height

            camera_group.add(tile)
            