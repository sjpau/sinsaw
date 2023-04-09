import pygame
import mapper

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        image = pygame.image.load("asset/player.jpg").convert_alpha()
        self.image = pygame.transform.scale(image, (mapper.tile_size, mapper.tile_size))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 1
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed