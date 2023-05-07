import pygame
import debug
import mapper

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(400, 100)
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    def attach_to(self, target):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def custom_draw(self):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    
    def in_view(self, go1, go2, tiles):
        start_pos = [go1.rect.centerx, go1.rect.centery] 
        end_pos = [go2.rect.centerx, go2.rect.centery] 
        thiccness = 5
        color = pygame.Color(181, 0, 255, 0)
        line = pygame.draw.line(self.display_surface, color, start_pos, end_pos, thiccness) 
        for tile in tiles:
            if mapper.status_transparent not in tile.status:
                if line.colliderect(tile.rect):
                    return True
            

        
