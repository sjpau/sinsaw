import pygame
import defs.finals as finals

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)

    def resize(self, surface, target):
        self.display_surface = surface
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

    def attach_to(self, target):
        x = target.rect.bottomright[0]
        y = target.rect.bottomright[1]
        self.offset.x = x - self.half_width
        self.offset.y = y - self.half_height

    def custom_draw(self):
        for sprite in self.sprites():
            if sprite.rect:
                offset_pos = sprite.rect.center - self.offset
                self.display_surface.blit(sprite.image, offset_pos)