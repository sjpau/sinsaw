import json
import os

class Level:
    def __init__(self, name, num, layout):
        self.name = name
        self.num = num
        self.layout = layout
    
    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def get_layout(self):
        return self.layout

def read_lvl_from_json(json_path):
    try:
        with open(json_path, 'r') as lvl:
            config = json.load(lvl)
        
        layout = config['layout']
        name = config['name']
        number = config['number']

    except Exception as e:
        print('Error when opening {json_path}: {e}')

    return name, number, layout