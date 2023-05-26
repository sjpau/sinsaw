import pygame
import defs.finals as finals
import loader.mapper as mapper

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)

    def resize(self, width, height, target):
        self.display_surface = pygame.display.set_mode((width, height))
        self.offset.x = target.rect.centerx - self.display_surface.get_width() / 2
        self.offset.y = target.rect.centery - self.display_surface.get_height() / 2

    def attach_to(self, target):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def custom_draw(self):
        for sprite in self.sprites():
            if sprite.rect:
                offset_pos = sprite.rect.center - self.offset
                self.display_surface.blit(sprite.image, offset_pos)