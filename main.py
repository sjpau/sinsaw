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
main_clock = pygame.time.Clock()

camera_group = camera.Camera()
lvl_example = level.init(os.path.join("lvl", "example.json"))
# Initialize map
tiles = mapper.init_tileset(lvl_example.layout, camera_group)
tileset_pixel_size = mapper.tileset_pixel_size(lvl_example.layout, mapper.tile_size)

# Initialize player
player_spawn_pos = lvl_example.get_player_spawn()
player_object = player.Player(player_spawn_pos, mapper.pos_to_xy(player_spawn_pos, lvl_example.layout, tiles), camera_group)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        #if event.type == pygame.VIDEORESIZE:


    # Do logical updates here.
    camera_group.attach_to(player_object)
    camera_group.update(lvl_example.layout, tiles)
    # Render the graphics here.
    screen.fill('black')
    camera_group.custom_draw()

    pygame.display.flip()

    main_clock.tick(60)
