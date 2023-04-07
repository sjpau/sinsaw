import sys
sys.path.insert(0, './loader') # TODO: orginize import the proper way
import loader
import os
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    ### REMOVABLE TEST CODE ###
    lvl_example_json_path = os.path.join('lvl', 'example.json')
    lvl_example_name, lvl_example_number, lvl_example_layout = loader.read_lvl_from_json(lvl_example_json_path) 
    lvl_example = loader.Level(lvl_example_name, lvl_example_number, lvl_example_layout)
    print(lvl_example_layout)
    ### REMOVABLE TEST CODE ###

    screen.fill("purple")

    # Render the graphics here.
    # ...

    pygame.display.flip()
    clock.tick(60)
