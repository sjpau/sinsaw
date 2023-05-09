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
        self.direction = pygame.math.Vector2(1, 0)
        self.category = 0
        self.path = []
        self.player_in_view = False

    def move_on_path(self):
        if not self.player_in_view:
            self.path = self.path[1:]
        if len(self.path) > 1:
            self.pos[0] = self.path[1][0]
            self.pos[1] = self.path[1][1]

    def to_axis_path(self, layout_binary, start_pos, end_pos):
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
        self.path = path

    def to_point_path(self, layout_binary, start_pos, end_pos):
        grid = Grid(matrix = list(zip(*layout_binary)))
        start = grid.node(start_pos[0], start_pos[1])
        end = grid.node(end_pos[0], end_pos[1])
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        path, _ = finder.find_path(start, end, grid)
        self.path = path

    def update(self, layout, tiles):

        xy = mapper.pos_to_xy(self.pos, layout, tiles)
        self.rect.x = xy[0]
        self.rect.y = xy[1]


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

