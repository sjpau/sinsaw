import pygame
from math import atan2, degrees
import helper.misc as misc

class DeadImage():
    def __init__(self, image, position, direction, size_x, size_y):
        self.position = position
        self.direction = direction
        self.angle = degrees(atan2(self.direction[1], self.direction[0])) % 360
        self.size_x = size_x
        self.size_y = size_y
        self.image = pygame.transform.scale(pygame.transform.rotate(image, self.angle), (self.size_x, self.size_y))
        self.rect = self.image.get_rect()

    def update(self, layout, tiles, items=None):
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
    
    def draw(self, screen, camera):
        offset_pos = self.position - camera.offset
        screen.blit(self.image, (int(offset_pos.x), int(offset_pos.y)))