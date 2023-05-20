import os
import pygame
import sys
import loader.loader as loader
import entity.camera as camera
import screen as s

class Level:
    def __init__(self, name, num, layout, player_spawn, enemy_spawns, item_spawns, exit_spawn):
        self.name = name
        self.num = num
        self.layout = layout
        self.player_spawn = player_spawn
        self.enemy_spawns = enemy_spawns
        self.item_spawns = item_spawns
        self.exit_spawn = exit_spawn
    
    def layout_to_binary(self, codes):
        layout_binary = []
        for i in range(len(self.layout)):
            row = []
            for j in range(len(self.layout[i])):
                if self.layout[i][j] in codes:
                    row.append(1)
                else:
                    row.append(0)
            layout_binary.append(row)
        return layout_binary