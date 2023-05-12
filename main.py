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
import enemy
import item
import debug 

pygame.init()
screen = pygame.display.set_mode((s.width,s.height),pygame.RESIZABLE)
main_clock = pygame.time.Clock()
codes_walkable = [0, 2, 6]

camera_group = camera.Camera()
lvl_example = level.init(os.path.join("lvl", "example.json"))
lvl_current = lvl_example
# Initialize map
tiles = mapper.init_tileset(lvl_current.layout, camera_group)
tileset_pixel_size = mapper.tileset_pixel_size(lvl_current.layout, mapper.tile_size)
layout_walkable = level.layout_to_binary(lvl_current.layout, codes_walkable)

# Initialize player
player_spawn_pos = lvl_current.get_player_spawn()
player_object = player.Player(player_spawn_pos, mapper.pos_to_xy(player_spawn_pos, lvl_current.layout, tiles), camera_group)
enemies = enemy.init_enemies(lvl_current.enemy_spawns, lvl_current.layout, tiles, camera_group)
items = item.init_items(lvl_current.item_spawns, lvl_current.layout, tiles, camera_group)
turn = 0
turn_ptr = turn

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        #if event.type == pygame.VIDEORESIZE:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                turn += 1
                player_object.move_left(lvl_current.layout, tiles)
            if event.key == pygame.K_d:
                turn += 1
                player_object.move_right(lvl_current.layout, tiles)
            if event.key == pygame.K_w:
                turn += 1
                player_object.move_up(lvl_current.layout, tiles)
            if event.key == pygame.K_s:
                turn += 1
                player_object.move_down(lvl_current.layout, tiles)

    # Do logical updates here.
    if turn != turn_ptr: 
        for e in enemies:
            e.behave(layout_walkable, tiles, camera_group, player_object)
        for i in items:
            if i.discarded:
                camera_group.remove(i)
                items.remove(i)
                del i
        turn_ptr = turn
        camera_group.update(lvl_current.layout, tiles, items)
    camera_group.attach_to(player_object)
    

    # Render the graphics here.
    screen.fill(pygame.Color(16, 13, 19))
    camera_group.custom_draw()
    # Allow debug in debug.py
    if debug.status:
        debug.display(pygame.mouse.get_pos())
        debug.display(player_object.pos, 40)
        debug.display("tile index: " + str(player_object.on_tile_index(lvl_current.layout, tiles)), 70)
        debug.display("direction: " + str(player_object.direction), 100)
        debug.display("tile status: " + str(tiles[player_object.on_tile_index(lvl_current.layout, tiles)].status), 160)
        debug.display("turn: " + str(turn), 220)
        if player_object.attached_item is not None:
            debug.display("attached: " + player_object.attached_item.name, 250)

    pygame.display.flip()
    main_clock.tick(60)