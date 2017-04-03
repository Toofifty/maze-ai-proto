from util import is_empty, draw_box

class Entity(object):
    def __init__(self, tiles, x, y, color, width=0):
        self.tiles = tiles
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def add_pos(self, dx, dy):
        if is_empty(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def set_pos(self, x, y):
        if is_empty(x, y):
            self.x = x
            self.y = y

    def draw(self):
        draw_box(self.x, self.y, self.color, self.width)
