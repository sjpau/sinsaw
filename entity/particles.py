import pygame
import random
import helper.misc as misc

class Particle():
    def __init__(self, position, color, radius, glow_color, velocity=pygame.Vector2(0,0), tag=0): #0 does nothing, 1 is blood
        self.position = position
        self.color = color
        self.glow_color = glow_color
        self.radius = radius
        if velocity == pygame.Vector2(0,0):
            self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        else:
            self.velocity = velocity
        self.last = random.randint(4, 6)
        self.delete = False
        self.tag = tag

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
            screen.blit(misc.circle_surface(glow_radius, color=self.glow_color), (int(offset_pos.x - glow_radius), int(offset_pos.y - glow_radius)), special_flags=pygame.BLEND_RGB_ADD)