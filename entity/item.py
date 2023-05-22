import pygame
import loader.asset as asset
import entity.gameobject as gameobject
import loader.mapper as mapper
import finals

class Item(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group, image):
        super().__init__(group)
        self.animations = {}
        gameobject.GameObject.__init__(self, pos, xy, image, group, False, self.animations)
        self.category = 0
        self.ammo = 0
        self.dropped = True
        self.discarded = False
        self.image_ptr = self.image
        self.transparent = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.transparent.fill((0, 0, 0, 0))
        self.name = ''

    def play_sfx_pick(self):
        if self.category == 1:
            finals.sfx_ext_pickup.play()
        elif self.category == 2:
            finals.sfx_gun_pickup.play()
        elif self.category == 3:
            finals.sfx_knife_pickup.play()
        elif self.category == 4:
            finals.sfx_molotow_pickup.play()
        elif self.category == 5:
            finals.sfx_key_pickup.play()
    
    def play_sfx_shoot(self):
        if self.category == 1:
            finals.sfx_steam.play()
        elif self.category == 2:
            finals.sfx_shoot.play()
        elif self.category == 3:
            pass
        elif self.category == 4:
            finals.sfx_bottle_break.play()
            finals.sfx_flame.play()
        elif self.category == 5:
            pass

    def update(self, layout, tiles, items=None):
        if not self.dropped:
            self.image = self.transparent
        if mapper.pos_in_layout_borders(self.pos, layout):
            xy = mapper.pos_to_xy(self.pos, layout, tiles)
            self.rect.x = xy[0]
            self.rect.y = xy[1]