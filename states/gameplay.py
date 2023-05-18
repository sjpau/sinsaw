import pygame
from .state import State
import sys
import os
import random
import entity.level as level
import loader.loader as loader
import entity.player as player
import screen as s
import entity.camera as camera
import entity.enemy as enemy
import entity.item as item
import entity.gameobject as gameobject
import debug
import time 
import entity.particles as particles
import entity.tile as tile
import loader.mapper as mapper



class Gameplay(State):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"
        self.actions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'shoot': False
        }
        self.codes_walkable = [0, 2, 6, 8]
        self.camera_group = camera.Camera()
        self.lvl = loader.init_level(os.path.join("lvl", "example.json")) # TODO change to class argument
        self.tiles = mapper.init_tileset(self.lvl.layout, self.camera_group)
        self.tileset_pixel_size = mapper.tileset_pixel_size(self.lvl.layout, mapper.tile_size)
        self.layout_walkable = self.lvl.layout_to_binary(self.codes_walkable)
        player_spawn_pos = self.lvl.get_player_spawn()
        game_objects_unflattened = []
        self.game_objects = []
        self.player_object = player.Player(player_spawn_pos, mapper.pos_to_xy(player_spawn_pos, self.lvl.layout, self.tiles), self.camera_group)
        self.items = item.init_items(self.lvl.item_spawns, self.lvl.layout, self.tiles, self.camera_group)
        self.enemies = loader.init_enemies(self.lvl.enemy_spawns, self.lvl.layout, self.tiles, self.camera_group)
        game_objects_unflattened.append(self.items)
        game_objects_unflattened.append([self.player_object])
        game_objects_unflattened.append(self.enemies)
        self.game_objects = [obj for sublist in game_objects_unflattened for obj in sublist]
        self.particles_list = []
        self.turn = 0
        self.turn_ptr = self.turn

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        #if event.type == pygame.VIDEORESIZE:
        #    self.camera_group.resize(event.w, event.h, self.player_object)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.turn += 1
                self.player_object.move_up(self.lvl.layout, self.tiles)
               # self.actions['up'] = True
            if event.key == pygame.K_s:
                self.turn += 1
                self.player_object.move_down(self.lvl.layout, self.tiles)
               # self.actions['down'] = True
            if event.key == pygame.K_a:
                self.turn += 1
                self.player_object.move_left(self.lvl.layout, self.tiles)
               # self.actions['left'] = True
            if event.key == pygame.K_d:
                self.turn += 1
                self.player_object.move_right(self.lvl.layout, self.tiles)
               # self.actions['right'] = True
            if event.key == pygame.K_SPACE:
                self.turn += 1
                self.player_object.shoot(self.lvl.layout, self.tiles, self.game_objects, self.player_object.attached_item.category)
                self.player_object.attached_item.ammo -= 1
               # self.actions['shoot'] = True

    def update(self, dt):
        if not self.player_object.alive:
            self.camera_group.remove(self.player_object)
            self.game_objects.remove(self.player_object)
            del self.player_object
            pygame.quit()
            raise SystemExit
        
        for e in self.enemies:
            if e.pos == self.player_object.pos:
                e.combat_target(self.lvl.layout, self.tiles, self.player_object)
            if not e.alive:
                self.camera_group.remove(e)
                self.enemies.remove(e)
                self.game_objects.remove(e)
                del e

        if self.turn != self.turn_ptr: 
            for e in self.enemies:
                if e.locked_on_target and self.tiles[mapper.get_tile_index_from_layout(self.lvl.layout, self.tiles, self.player_object.pos)].affected != 2:
                    e.shoot(self.lvl.layout, self.tiles, self.game_objects, 2)
                    e.locked_on_target = False
                else:
                    e.behave(self.layout_walkable, self.tiles, self.camera_group, self.player_object)
            for i in self.items:
                if i.discarded:
                    self.camera_group.remove(i)
                    self.items.remove(i)
                    self.game_objects.remove(i)
                    del i
            self.turn_ptr = self.turn
            self.camera_group.update(self.lvl.layout, self.tiles, self.items)
        self.camera_group.attach_to(self.player_object)
        
        for t in self.tiles:
            if t.affected == 1: # Set on fire
                self.particles_list.append(particles.Particle(t.rect.bottomright, (255, 143, 0), random.randint(5, 10), (170, 61, 57), velocity=pygame.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))))
            elif t.affected == 2: # Set in fog
                self.particles_list.append(particles.Particle(t.rect.bottomright, (149, 165, 166), random.randint(10, 15), (20,20,20)))

        for i in self.particles_list:
            i.update()
            if i.delete:
                self.particles_list.remove(i)
                del i

    def draw(self, surface):
        surface.fill(pygame.Color(16, 13, 19))
        self.camera_group.custom_draw()
        for i in self.particles_list:
            i.draw(surface, self.camera_group)
        # Allow debug in debug.py
        if debug.status:
            debug.display(self.player_object.pos, 40)
            debug.display("tile index: " + str(self.player_object.on_tile_index(self.lvl.layout, self.tiles)), 70)
            debug.display("direction: " + str(self.player_object.direction), 100)
            debug.display("tile status: " + str(self.tiles[self.player_object.on_tile_index(self.lvl.layout, self.tiles)].status), 160)
            debug.display("turn: " + str(self.turn), 220)
            if self.player_object.attached_item is not None:
                debug.display("attached: " + self.player_object.attached_item.name, 250)
                debug.display("ammo: " + str(self.player_object.attached_item.ammo), 280)