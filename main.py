import sys
import os
import pygame
sys.path.insert(0, './loader') 
sys.path.insert(0, './entity') 
import level
import loader
import player
import screen as s
import camera 
import mapper 

pygame.init()
screen = pygame.display.set_mode((s.width,s.height))
clock = pygame.time.Clock()

camera_group = camera.Camera()
lvl_example = level.init(os.path.join("lvl", "example.json"))
# Initialize map
tiles = mapper.init_tileset(lvl_example.layout, camera_group)
tileset_pixel_size = mapper.tileset_pixel_size(lvl_example.layout, mapper.tile_size)

# Initialize player
player_spawn_pos = lvl_example.get_player_spawn()
player_spawn_tile_index = mapper.get_tile_index_from_layout(lvl_example.layout, tiles, player_spawn_pos)
player_spawn_xy = (tiles[player_spawn_tile_index].rect.x, tiles[player_spawn_tile_index].rect.y)
player_object = player.Player(player_spawn_xy, camera_group)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        #if event.type == pygame.VIDEORESIZE:


    # Do logical updates here.
    camera_group.attach_to(player_object)
    camera_group.update()
    # Render the graphics here.
    screen.fill('black')
    camera_group.custom_draw()

    pygame.display.flip()
    clock.tick(60)
