import pygame
import defs.finals as finals

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)

        self.camera_borders = {'left': 300, 'right': 300, 'top': 200, 'bottom':200}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_box = pygame.Rect(l,t,w,h)

    def resize(self, surface, target):
        self.display_surface = surface
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

    def attach_box_to(self, target):
        if target.rect.left < self.camera_box.left:
            self.camera_box.left = target.rect.left
        if target.rect.right > self.camera_box.right:
            self.camera_box.right = target.rect.right
        if target.rect.top < self.camera_box.top:
            self.camera_box.top = target.rect.top
        if target.rect.bottom > self.camera_box.bottom:
            self.camera_box.bottom = target.rect.bottom
        self.offset.x = self.camera_box.left - self.camera_borders['left']
        self.offset.y = self.camera_box.top - self.camera_borders['top']
    
    def attach_to(self, target):
        x = target.rect.bottomright[0]
        y = target.rect.bottomright[1]
        self.offset.x = x - self.half_width
        self.offset.y = y - self.half_height
        self.attach_box_to(target)


    def custom_draw(self):
        for sprite in self.sprites():
            if sprite.rect:
                offset_pos = sprite.rect.center - self.offset
                self.display_surface.blit(sprite.image, offset_pos)