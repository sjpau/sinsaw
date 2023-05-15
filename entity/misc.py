def slice_from_direction(layout, direction, pos, end_pos=None, skip_first=True):
    rows, cols = len(layout), len(layout[0])
    array = []
    x = pos[1]
    y = pos[0]

    while 0 <= y < rows and 0 <= x < cols:
        array.append([[y,x],layout[y][x]])
        y -= int(direction.y)
        x += int(direction.x)
        print(array)
    if end_pos is not None:
        index = array.index([end_pos, layout[end_pos[1], end_pos[0]]])
        array = array[index:]
        print(array)
    if skip_first:
        array.pop(0)
    
    return array
