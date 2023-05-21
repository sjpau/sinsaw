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
import finals



class Gameplay(State):
    def __init__(self, chapter, surface):
        super(Gameplay, self).__init__()
        self.surface = surface
        self.next_state = "GAME_OVER"
        self.codes_walkable = [0, 2, 6, 8, 3, 7]
        self.camera_group = camera.Camera()
        self.actions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'shoot': False
        }
        self.lvls = []
        self.on_lvl = 0
        self.lvl_final = len(chapter)
        for l in chapter:
            new_lvl = loader.init_level(os.path.join("lvl", l))
            self.lvls.append(new_lvl)
        self.lvl = self.lvls[self.on_lvl]
        # INIT LVL VARS
        self.tiles = mapper.init_tileset(self.lvl.layout, self.camera_group)
        self.tileset_pixel_size = mapper.tileset_pixel_size(self.lvl.layout, mapper.tile_size)
        self.layout_walkable = self.lvl.layout_to_binary(self.codes_walkable)
        self.player_spawn = self.lvl.player_spawn.copy()
        game_objects_unflattened = []
        self.game_objects = []
        self.player_object = player.Player(self.player_spawn, mapper.pos_to_xy(self.player_spawn, self.lvl.layout, self.tiles), self.camera_group)
        self.items = item.init_items(self.lvl.item_spawns, self.lvl.layout, self.tiles, self.camera_group)
        self.enemies = loader.init_enemies(self.lvl.enemy_spawns, self.lvl.layout, self.tiles, self.camera_group)
        game_objects_unflattened.append(self.items)
        game_objects_unflattened.append([self.player_object])
        game_objects_unflattened.append(self.enemies)
        self.game_objects = [obj for sublist in game_objects_unflattened for obj in sublist]
        self.particles_list = []
        self.turn = 0
        self.turn_ptr = self.turn
    
    def reinit(self):
        self.lvl = self.lvls[self.on_lvl]
        self.tiles = mapper.init_tileset(self.lvl.layout, self.camera_group)
        self.tileset_pixel_size = mapper.tileset_pixel_size(self.lvl.layout, mapper.tile_size)
        self.layout_walkable = self.lvl.layout_to_binary(self.codes_walkable)
        self.player_spawn = self.lvl.player_spawn.copy()
        game_objects_unflattened = []
        self.game_objects = []
        self.player_object = player.Player(self.player_spawn, mapper.pos_to_xy(self.player_spawn, self.lvl.layout, self.tiles), self.camera_group)
        self.items = item.init_items(self.lvl.item_spawns, self.lvl.layout, self.tiles, self.camera_group)
        self.enemies = loader.init_enemies(self.lvl.enemy_spawns, self.lvl.layout, self.tiles, self.camera_group)
        game_objects_unflattened.append(self.items)
        game_objects_unflattened.append([self.player_object])
        game_objects_unflattened.append(self.enemies)
        self.game_objects = [obj for sublist in game_objects_unflattened for obj in sublist]
        self.particles_list = []
        self.turn = 0

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.VIDEORESIZE:
            if not self.fullscreen:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.camera_group.resize(event.w, event.h, self.player_object)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.surface = pygame.display.set_mode((self.surface.get_width(), self.surface.get_height()), pygame.FULLSCREEN)
                    self.camera_group.resize(self.surface.get_width(), self.surface.get_height(), self.player_object)
                else:
                    self.surface = pygame.display.set_mode((self.surface.get_width(), self.surface.get_height()), pygame.RESIZABLE)
                    self.camera_group.resize(self.surface.get_width(), self.surface.get_height(), self.player_object)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.turn += 1
                self.actions['up'] = True
            if event.key == pygame.K_s:
                self.turn += 1
                self.actions['down'] = True
            if event.key == pygame.K_a:
                self.turn += 1
                self.actions['left'] = True
            if event.key == pygame.K_d:
                self.turn += 1
                self.actions['right'] = True
            if event.key == pygame.K_SPACE:
                if self.player_object.attached_item is not None:
                    if self.player_object.attached_item.ammo > 0:
                        self.turn += 1
                        self.actions['shoot'] = True

    def handle_actions(self):
        if self.actions['down']:
            self.player_object.move_down(self.lvl.layout, self.tiles)
            finals.sfx_step.play()
            self.actions['down'] = False
        elif self.actions['up']:
            self.player_object.move_up(self.lvl.layout, self.tiles)
            finals.sfx_step.play()
            self.actions['up'] = False
        elif self.actions['right']:
            self.player_object.move_right(self.lvl.layout, self.tiles)
            finals.sfx_step.play()
            self.actions['right'] = False
        elif self.actions['left']:
            self.player_object.move_left(self.lvl.layout, self.tiles)
            finals.sfx_step.play()
            self.actions['left'] = False
        elif self.actions['shoot']:
            if self.player_object.attached_item is not None:
                self.player_object.shoot(self.lvl.layout, self.tiles, self.game_objects, self.player_object.attached_item.category, self.particles_list)
                self.player_object.attached_item.ammo -= 1
                self.player_object.attached_item.play_sfx_shoot()
                self.actions['shoot'] = False
        
    def update(self, dt):

        if not self.player_object.alive:
            self.camera_group.remove(self.player_object)
            self.game_objects.remove(self.player_object)
            self.reinit()
        if self.player_object.pos == self.lvl.exit_spawn:
            if self.on_lvl != self.lvl_final - 1:
                self.on_lvl += 1
                self.reinit() 
        if self.enemies:
            for e in self.enemies:
                if not e.locked_on_target:
                    self.handle_actions()
                if e.pos == self.player_object.pos:
                    e.combat_target(self.lvl.layout, self.tiles, self.player_object, self.particles_list)
                if not e.alive:
                    self.camera_group.remove(e)
                    self.enemies.remove(e)
                    self.game_objects.remove(e)
                    del e
                    break
        else:
            self.handle_actions()

        if self.turn != self.turn_ptr: 
            for e in self.enemies:
                if e.locked_on_target and self.tiles[mapper.get_tile_index_from_layout(self.lvl.layout, self.tiles, self.player_object.pos)].affected != 2:
                    e.shoot(self.lvl.layout, self.tiles, self.game_objects, 2, self.particles_list)
                    finals.sfx_shoot_enemy.play()
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

        p_on_tile =  self.player_object.on_tile_index(self.lvl.layout, self.tiles)
        if mapper.status['breachable'] in self.tiles[p_on_tile].status:
            finals.sfx_door_break_1.play()
            finals.sfx_door_break_2.play()
            self.tiles[p_on_tile].status.remove(mapper.status['breachable'])
            self.tiles[p_on_tile].status.append(mapper.status['transparent'])
            self.tiles[p_on_tile].status.append(mapper.status['walkable'])
        for t in self.tiles:
            if t.affected == 1: # Set on fire
                self.particles_list.append(particles.Particle(t.rect.bottomright, finals.COLOR_ORANGE, random.randint(5, 10), finals.COLOR_RED_SUBTLE, velocity=pygame.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))))
            elif t.affected == 2: # Set in fog
                self.particles_list.append(particles.Particle(t.rect.bottomright, finals.COLOR_GREY, random.randint(10, 15), finals.COLOR_GREY_DARK))

        for i in self.particles_list:
            i.update()
            if i.delete:
                self.particles_list.remove(i)
                del i

    def draw(self):
        self.surface.fill(finals.COLOR_BLACK)
        self.camera_group.custom_draw()
        for i in self.particles_list:
            i.draw(self.surface, self.camera_group)
        # Allow debug in debug.py
        if debug.status:
            debug.display(str(self.player_object.pos) + str(self.lvl.player_spawn), 40)
            debug.display("tile index: " + str(self.player_object.on_tile_index(self.lvl.layout, self.tiles)), 70)
            debug.display("direction: " + str(self.player_object.direction), 100)
            debug.display("tile status: " + str(self.tiles[self.player_object.on_tile_index(self.lvl.layout, self.tiles)].status), 160)
            debug.display("turn: " + str(self.turn), 220)
            if self.player_object.attached_item is not None:
                debug.display("attached: " + self.player_object.attached_item.name, 250)
                debug.display("ammo: " + str(self.player_object.attached_item.ammo), 280)