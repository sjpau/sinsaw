import pygame
import gameobject
import mapper
import asset
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Enemy(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group):
        super().__init__(group)
        image = pygame.image.load(asset.image_enemy).convert_alpha()
        gameobject.GameObject.__init__(self, pos, xy, image, False)
        self.category = 0
        self.path = []
        self.player_in_view = False
        self.locked_on_target = False

    def set_direction(self):
        if len(self.path) > 1:
            y1, x1 = self.path[0]
            y2, x2 = self.path[1]
            delta_x = x2 - x1
            delta_y = y2 - y1
            if delta_x > 0 and delta_y == 0:
                self.direction[0] = 1
                self.direction[1] = 0
            elif delta_x < 0 and delta_y == 0:
                self.direction[0] = -1
                self.direction[1]= 0
            elif delta_x == 0 and delta_y > 0:
                self.direction[0] = 0
                self.direction[1] = -1
            elif delta_x == 0 and delta_y < 0:
                self.direction[0] = 0
                self.direction[1] = 1

    def move_on_path(self):
        #self.direction_ptr = self.direction.copy()
        self.set_direction()
        if not self.player_in_view:
            self.path = self.path[1:]
        if len(self.path) > 1:
            self.pos[0] = self.path[1][0]
            self.pos[1] = self.path[1][1]
    
    def step(self, layout, tiles):
        next_pos = [0,0]
        if self.direction[1] > 0:
            next_pos[0] = self.pos[0] - int(self.direction[1])
        else:
            next_pos[0] = self.pos[0] + abs(int(self.direction[1]))
        next_pos[1] = self.pos[1] + int(self.direction[0])
        if gameobject.pos_in_layout_borders(next_pos, layout):
            next_tile = tiles[mapper.get_tile_index_from_layout(layout, tiles, next_pos)]
            for status in next_tile.status:
                if status == mapper.status_walkable:
                    if self.direction[1] < 0 or self.direction[0] < 0:
                        self.pos[0] += abs(int(self.direction[1]))
                        self.pos[1] += int(self.direction[0])
                    elif self.direction[1] > 0:
                        self.pos[0] -= int(self.direction[1])
                        self.pos[1] += int(self.direction[0])
                    elif self.direction[0] > 0:
                        self.pos[0] += int(self.direction[1])
                        self.pos[1] += int(self.direction[0])


    def to_axis_path(self, layout_binary, start_pos, end_pos):
        start_pos = (start_pos[0], start_pos[1])
        end_pos = (end_pos[0], end_pos[1])
        marginx = abs(start_pos[0] - end_pos[0])
        marginy = abs(start_pos[1] - end_pos[1])
        if marginx < marginy:
            # Move to x-axis
            to_axis = (end_pos[0], start_pos[1])
        else:
            # Move to y-axis
            to_axis = (start_pos[0], end_pos[1])
        grid = Grid(matrix = list(zip(*layout_binary)))
        start = grid.node(start_pos[0], start_pos[1])
        end = grid.node(to_axis[0], to_axis[1])
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        path, _ = finder.find_path(start, end, grid)
        self.destination = end_pos
        self.path = path

    def to_point_path(self, layout_binary, start_pos, end_pos):
        grid = Grid(matrix = list(zip(*layout_binary)))
        start = grid.node(start_pos[0], start_pos[1])
        end = grid.node(end_pos[0], end_pos[1])
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        path, _ = finder.find_path(start, end, grid)
        self.destination = end_pos
        self.path = path
    
    def to_direction(self, start_pos, end_pos):
        x1, y1 = start_pos
        x2, y2 = end_pos
        if x1 == x2 and y1 != y2:
            if y1 - y2 < 0:
                self.direction = [1, 0]
            else:
                self.direction = [-1, 0]
        elif y1 == y2 and x1 != x2:
            if x1 - x2 < 0:
                self.direction = [0, -1]
            else:
                self.direction = [0, 1]
    
    def clockwise_direction(self):
        self.direction_ptr = self.direction.copy()
        if self.direction == pygame.math.Vector2(1, 0):
            self.direction = pygame.math.Vector2(0, -1)
        elif self.direction == pygame.math.Vector2(0, 1):
            self.direction = pygame.math.Vector2(1, 0)
        elif self.direction == pygame.math.Vector2(-1, 0):
            self.direction = pygame.math.Vector2(0, 1)
        elif self.direction == pygame.math.Vector2(0, -1):
            self.direction = pygame.math.Vector2(-1, 0)
    
    def default_behaviour(self, layout, tiles, camera_group, player_object):
        if self.category == 1:
            self.clockwise_direction()
            self.step(layout, tiles)
            self.step(layout, tiles)
        elif self.category == 2:
            self.clockwise_direction()
            self.step(layout, tiles)

    def to_target(self, layout, tiles, target):
        if target.pos[0] == self.pos[0] or target.pos[1] == self.pos[1]:
            self.to_direction(self.pos, target.pos)
            self.step(layout, tiles)
            self.locked_on_target = True

    def behave(self, layout, tiles, camera_group, player_object):
        self.direction_ptr = self.direction.copy()
        if self.category == 1: # Active behavior of melee enemy
            if not camera_group.in_view(self, player_object, tiles):
                self.player_in_view = True
                self.to_point_path(layout, self.pos, player_object.pos)
            else:
                self.player_in_view = False
            if len(self.path) == 0:
                self.default_behaviour(layout, tiles, camera_group, player_object)
            else:
                self.move_on_path()
        if self.category == 2: # Active behaviour of ranged enemy
            if not camera_group.in_view(self, player_object, tiles):
                self.player_in_view = True
                self.to_axis_path(layout, self.pos, player_object.pos)
                if self.locked_on_target:
                    self.locked_on_target = False
                    #Shoot
                else:
                    self.to_target(layout, tiles, player_object)
            else:
                self.player_in_view = False
            self.move_on_path()
            if len(self.path) == 0:
                self.default_behaviour(layout, tiles, camera_group, player_object)

    def update(self, layout, tiles, items=None):
        if gameobject.pos_in_layout_borders(self.pos, layout):
            xy = mapper.pos_to_xy(self.pos, layout, tiles)
            self.rect.x = xy[0]
            self.rect.y = xy[1]
            gameobject.update(self)


def init_enemies(enemy_spawns, layout, tiles, group):
    enemies = []
    for row in enemy_spawns:
        pos = [row[0], row[1]]
        category = row[2]
        xy = mapper.pos_to_xy(pos, layout, tiles)
        enemy = Enemy(pos, xy, group)
        enemy.category = category
        enemies.append(enemy)
    
    return enemies

