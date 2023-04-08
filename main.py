import sys
import os
import pygame
sys.path.insert(0, './loader') # TODO: orginize import the proper way
sys.path.insert(0, './entity') # TODO: orginize import the proper way
import level
import loader
import player
import screen as s
import camera 
import mapper 

pygame.init()
screen = pygame.display.set_mode((s.width,s.height))
clock = pygame.time.Clock()

### REMOVABLE TEST CODE ###
camera_group = camera.Camera()
lvl_example = level.init(os.path.join("lvl", "example.json"))
#margin = level.margin(lvl_example.layout, mapper.tile_size)
player_spawn_pos = lvl_example.get_player_spawn()
player_object = player.Player(player_spawn_pos, camera_group)
mapper.init(lvl_example.layout, camera_group)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


    # Do logical updates here.
    # ...
    
    screen.fill("purple")

    # Render the graphics here.
    # ...
    camera_group.custom_draw(screen)
    screen.blit(player_object.image, player_object.rect)
    player_object.update()

    pygame.display.flip()
    clock.tick(60)
