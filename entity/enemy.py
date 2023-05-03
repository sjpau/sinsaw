import pygame
import gameobject
import mapper

class Enemy(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group):
        super().__init__(group)
        gameobject.GameObject.__init__(self, pos)
        image = pygame.image.load("asset/lame.png").convert_alpha()
        self.image = pygame.transform.scale(image, (mapper.tile_size, mapper.tile_size))
        self.rect = self.image.get_rect(topleft = xy)
        self.direction = pygame.math.Vector2(1, 0)
        self.category = 0

def init_enemies(enemy_spawns, layout, tiles, group):

    enemies = []
    for row in enemy_spawns:
        pos = [row[0], row[1]]
        category = row[2]
        xy = mapper.pos_to_xy(pos, layout, tiles)
        enemy = Enemy(pos, xy, group)
        enemies.append(enemy)
    
    return enemies