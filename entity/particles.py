import pygame
import random

def circle_surface(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius, pygame.SRCALPHA)
    surf.set_colorkey((0, 0, 0))
    surf.set_alpha(100)
    return surf

class Particle():
    def __init__(self, position, color, radius, glow_color):
        self.position = position
        self.color = color
        self.glow_color = glow_color
        self.radius = radius
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.last = random.randint(4, 6)
        self.delete = False

    def update(self):
        self.position += self.velocity
        self.radius -= 0.1
        if self.radius <= 0:
            self.delete = True

    def draw(self, screen, camera, glow=True):
        offset_pos = self.position - camera.offset
        pygame.draw.circle(screen, self.color, (int(offset_pos.x), int(offset_pos.y)), int(self.radius))
        if glow:
            glow_radius = self.radius * 2
            screen.blit(circle_surface(glow_radius, color=self.glow_color), (int(offset_pos.x - glow_radius), int(offset_pos.y - glow_radius)), special_flags=pygame.BLEND_RGB_ADD)
