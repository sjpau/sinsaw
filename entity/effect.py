import pygame
import entity.gameobject as gameobject
from entity.animation import Animation
import loader.anims as anims
import loader.mapper as mapper

class Effect(gameobject.GameObject):
    def __init__(self, pos, xy, image):
        anim_active_fire, anim_active_smoke = anims.load_animation_effects()
        animations_effects = {
            'fire': Animation(anim_active_fire, 70),
            'smoke': Animation(anim_active_smoke, 100),
        }
        gameobject.GameObject.__init__(self, pos, xy, image, False, None, animations_effects)

    def draw(self, screen, camera):
        offset_pos = self.rect.bottomright - camera.offset
        screen.blit(self.image, (int(offset_pos.x), int(offset_pos.y)))