import pygame
import entity.gameobject as gameobject
import loader.mapper as mapper
import entity.particles as particles
import random
import defs.finals as finals

class Tile(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, group, image):
        super().__init__(group)
        pos = [0,0]
        gameobject.GameObject.__init__(self, pos, pos, image, group, True)
        self.code = -1
        self.status = []
        self.affected = 0 # 1 - Fire, 2 - Fog
    
    def on_shot(self, particles_list):
        super().on_shot(particles_list)
        if self.code == 4 or self.code == 5: # Glass
            finals.sfx_glass_on_shot.play()
            for i in range(20):
                particles_list.append(particles.Particle(self.rect.bottomright, finals.COLOR_BEIGE, random.randint(1, 4), finals.COLOR_BEIGE, velocity=pygame.Vector2(random.uniform(-5, 10), random.uniform(-5, 10))))
        elif self.code == 2 or self.code == 3 or self.code == 6 or self.code == 7: # Doors
            finals.sfx_door_on_shot.play()
            for i in range(20):
                particles_list.append(particles.Particle(self.rect.bottomright, finals.COLOR_BEIGE, random.randint(1, 4), finals.COLOR_BEIGE, velocity=pygame.Vector2(random.uniform(-5, 10), random.uniform(-5, 10))))
        elif self.code == 1: # Wall
            for i in range(10):
                particles_list.append(particles.Particle(self.rect.bottomright, finals.COLOR_PURPLE, random.randint(1, 4), finals.COLOR_PURPLE, velocity=pygame.Vector2(random.uniform(-5, 1), random.uniform(-5, 1))))

    def change_image(self):
        if self.code == 2: 
            self.image = finals.image_door_broken_2
        elif self.code == 3:
            self.image = finals.image_door_broken_1
        elif self.code == 6:
            self.image = finals.image_door_unlocked_2
        elif self.code == 7:
            self.image = finals.image_door_unlocked_1

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