import json
import os

def read_lvl_from_json(json_path):
    try:
        with open(json_path, 'r') as lvl:
            config = json.load(lvl)
        
        layout = config['layout']
        name = config['name']
        number = config['number']
        spawn_player = config['spawn_player']

    except Exception as e:
        print('Error when opening {json_path}: {e}')

    return name, number, layout, spawn_player