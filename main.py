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


#mapper.tileset_upd_pos(screen, tiles, tileset_pixel_size[0], tileset_pixel_size[1])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        #if event.type == pygame.VIDEORESIZE:
            #mapper.tileset_upd_pos(screen, tiles, tileset_pixel_size[0], tileset_pixel_size[1])


    player_object.update()
    # Do logical updates here.
    camera_group.update()
    # Render the graphics here.
    camera_group.custom_draw(screen)
   # player_object.image = pygame.transform.scale(player_object.image, (32, 32))
   # screen.blit(player_object.image, player_object.rect)

    pygame.display.flip()
    clock.tick(60)
