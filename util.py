import pygame

surface = None
tile_size = 0
tiles = []

def init(_surface, _tile_size, _tiles):
    global surface
    global tile_size
    global tiles
    surface = _surface
    tile_size = _tile_size
    tiles = _tiles

def draw_box(x, y, color, width=0):
    global surface
    global tile_size
    pygame.draw.rect(surface, color, (x * tile_size, y * tile_size, tile_size,
        tile_size), width)

def is_empty(x, y):
    global tiles
    return tiles[y][x] == 0
