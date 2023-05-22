import pygame
import loader.mapper as mapper

class Animation():
    def __init__(self, sprites, speed):
        self.sprites = sprites
        for sprite in self.sprites:
            image = pygame.transform.scale(sprite, (mapper.tile_size, mapper.tile_size))
            sprite = image
        self.speed = speed
        self.current_sprite = 0
    
    def get_current_sprite(self):
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        return self.sprites[int(self.current_sprite)]
    
    def get_sprite(self, i):
        return self.sprites[i]

    def play(self):
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.current_sprite += self.speed