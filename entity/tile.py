import pygame
import entity.gameobject as gameobject
import loader.mapper as mapper

class Tile(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, group, image):
        super().__init__(group)
        pos = [0,0]
        gameobject.GameObject.__init__(self, pos, pos, image, True)
        self.code = -1
        self.status = []
        self.affected = 0 # 1 - Fire, 2 - Fog
    
    def init_status(self):
        if self.code == 0: # Tile 
            self.status = [mapper.status['walkable'], mapper.status['transparent']] 
        elif self.code == 8: # Tile
            self.status = [mapper.status['walkable'], mapper.status['transparent']] 
        elif self.code == 9: # Empty Tile
            self.status = [mapper.status['transparent']]
        elif self.code == 1: # Wall
            self.status = [mapper.status['indestructable']]
        elif self.code == 2: # Door
            self.status = [mapper.status['breachable']]
        elif self.code == 3: # Door
            self.status = [mapper.status['breachable']]
        elif self.code == 4: # Glass
            self.status = [mapper.status['destructable'], mapper.status['transparent']]
        elif self.code == 5: # Glass
            self.status = [mapper.status['destructable'], mapper.status['transparent']]
        elif self.code == 6: # Locked door
            self.status = [mapper.status['unlockable']]
        elif self.code == 7: # Locked door
            self.status = [mapper.status['unlockable']]