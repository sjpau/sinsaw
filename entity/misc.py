import pygame

def slice_from_direction(layout, direction, pos, end_in=None, skip_first=True):
    rows, cols = len(layout), len(layout[0])
    array = []
    x = pos[1]
    y = pos[0]
    while 0 <= y < rows and 0 <= x < cols:
        array.append([y,x])
        y -= int(direction.y)
        x += int(direction.x)
        if end_in is not None:
            end_in -= 1
        if end_in == 0:
            break
    if skip_first and array != []:
        array.pop(0)
    
    return array

def set_direction():
    up = pygame.math.Vector2(0, 1)
    down = pygame.math.Vector2(0, -1)
    right = pygame.math.Vector2(1, 0)
    left = pygame.math.Vector2(-1, 0)
    return up, down, right, left

def molotow_slice(layout, pos, h_area=3, v_area=3):
    direction_up, direction_down, direction_right, direction_left = set_direction()

    molotow_slice = []
    vertical_slice = []
    vertical_slice.append(pos)
    up_slice = slice_from_direction(layout, direction_up, pos, end_in=v_area)
    down_slice = slice_from_direction(layout, direction_down, pos, end_in=v_area)
    for i in up_slice:
        vertical_slice.append(i)
    for i in down_slice:
        vertical_slice.append(i)
    for coord in vertical_slice:

        horizontal_left = slice_from_direction(layout, direction_left, coord, end_in=h_area)
        horizontal_right = slice_from_direction(layout, direction_right, coord, end_in=h_area)
        for i in horizontal_left:
            molotow_slice.append(i)
        for i in horizontal_right:
            molotow_slice.append(i)
    for i in vertical_slice:
        molotow_slice.append(i)

    return molotow_slice