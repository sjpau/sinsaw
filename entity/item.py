import pygame
import mapper
import asset
import gameobject

class Item(pygame.sprite.Sprite, gameobject.GameObject):
    def __init__(self, pos, xy, group, image):
        super().__init__(group)
        gameobject.GameObject.__init__(self, pos, xy, image, False)
        self.category = 0
        self.ammo = 0
        self.dropped = True
        self.discarded = False
        self.image_ptr = self.image
        self.transparent = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.transparent.fill((0, 0, 0, 0))
        self.name = ''
    
    def update(self, layout, tiles, items=None):
        if not self.dropped:
            self.image = self.transparent
        if self.discarded:
            self.dropped = True
            self.image = self.image_ptr
        if gameobject.pos_in_layout_borders(self.pos, layout):
            xy = mapper.pos_to_xy(self.pos, layout, tiles)
            self.rect.x = xy[0]
            self.rect.y = xy[1]
            gameobject.update(self)

def init_items(item_spawns, layout, tiles, group):
    items = []
    for row in item_spawns:
        pos = [row[0], row[1]]
        category = row[2]
        ammo = row[3]
        xy = mapper.pos_to_xy(pos, layout, tiles)
        if category == 1:
            image = pygame.image.load(asset.item_exting).convert_alpha()
            name = 'fire extinguisher'
        elif category == 2:
            image = pygame.image.load(asset.item_gun).convert_alpha()
            name = 'pistol'
        elif category == 3:
            image = pygame.image.load(asset.item_knife).convert_alpha()
            name = 'combat knife'
        elif category == 4:
            image = pygame.image.load(asset.item_molotow).convert_alpha()
            name = 'molotow cocktail'
        elif category == 5:
            image = pygame.image.load(asset.item_key).convert_alpha()
            name = 'key'
        item = Item(pos, xy, group, image)
        item.category = category
        item.ammo = ammo
        item.name = name
        items.append(item)
    
    return items