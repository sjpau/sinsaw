import sys
sys.path.insert(0, './loader') # TODO: orginize import the proper way
import loader
import os
import pygame

pygame.init()
screen_height = 1080
screen_width = 1920
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

### REMOVABLE TEST CODE ###
rect_size = 32

lvl_example_json_path = os.path.join('lvl', 'example.json')
lvl_example_name, lvl_example_number, lvl_example_layout = loader.read_lvl_from_json(lvl_example_json_path) 
lvl_example = loader.Level(lvl_example_name, lvl_example_number, lvl_example_layout)

lvl_width = len(lvl_example_layout[0]) * (rect_size)
lvl_height = len(lvl_example_layout) * (rect_size)
x = (screen_width - lvl_width) // 2
y = (screen_height - lvl_height) // 2
### REMOVABLE TEST CODE ###

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    ### REMOVABLE TEST CODE ###

    ### REMOVABLE TEST CODE ###

    screen.fill("purple")

    # Render the graphics here.
    # ...
    for row in range(len(lvl_example_layout)):
        for col in range(len(lvl_example_layout[row])):
            if lvl_example_layout[row][col] == 0:
                color = (255, 0, 0)
            elif lvl_example_layout[row][col] == 1:
                color = (0, 255, 0)
            elif lvl_example_layout[row][col] == 2:
                color = (0, 0, 255)
            
            print(screen_height,screen_width)
        
            rect_x =  x + col * rect_size
            rect_y =  y + row * rect_size

            pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, rect_size, rect_size))


    pygame.display.flip()
    clock.tick(60)
