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
    
    def move_down(self):
        self.direction.y = 1
        self.direction.x = 0
        self.pos[0] += 1

    def move_up(self):
        self.direction.y = -1
        self.direction.x = 0
        self.pos[0] -= 1

    def move_left(self):
        self.direction.x = -1
        self.direction.y = 0
        self.pos[1] -= 1

    def move_right(self):
        self.direction.x = 1
        self.direction.y = 0
        self.pos[1] += 1

  
    def update(self, layout, tiles):

        MAX = len(layout)
        MIN = 0
        if self.pos[0] < MIN: 
            self.pos[0] = MIN
        elif self.pos[0] >= MAX:
            self.pos[0] = MAX - 1
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= MAX:
            self.pos[1] = MAX - 1 

        xy = mapper.pos_to_xy(self.pos, layout, tiles)
        self.rect.x = xy[0]
        self.rect.y = xy[1]