import pygame
from pygame.locals import *
import ai, entity, util
import thread

def main():
    framecount = 0
    exit = False
    nodes = []
    tiles = load_tiles()

    tile_size = 16

    pygame.init()
    pygame.display.set_caption("Monster AI Prototype")
    screen = pygame.display.set_mode((len(tiles) * tile_size, len(tiles) * tile_size))
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    util.init(background, tile_size, tiles)

    nodes = ai.init(len(tiles))

    key_player = entity.Entity(tiles, 1, 1, (255, 0, 0))
    mouse_player = entity.Entity(tiles, len(tiles) - 2, 1, (0, 255, 0))
    monster = entity.Entity(tiles, int(len(tiles) / 2), int(len(tiles) / 2),
            (0, 0, 0))

    while not exit:
        clock.tick(60)
        screen.blit(background, (0, 0))
        draw_tiles(background, tiles, tile_size)

        key_player.draw()
        mouse_player.draw()
        monster.draw()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and
                    event.key == K_ESCAPE):
                return

            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    key_player.add_pos(0, 1)

                elif event.key == K_UP:
                    key_player.add_pos(0, -1)

                elif event.key == K_LEFT:
                    key_player.add_pos(-1, 0)

                elif event.key == K_RIGHT:
                    key_player.add_pos(1, 0)

        mx, my = pygame.mouse.get_pos()
        mouse_player.set_pos(mx / tile_size, my / tile_size)

        ai_move = ai.ai_step(framecount, nodes, monster, (mouse_player,))

        framecount += 1
        pygame.display.flip()


def load_tiles():
    tiles = []
    with open("map.txt", "r") as f:
        strings = f.read().strip().split("\n")

    for j in range(0, len(strings)):
        tiles.append([])
        for i in range(0, len(strings[0])):
            tiles[j].append(1 if strings[j][i] == "#" else 0)
    return tiles


def draw_tiles(surf, tiles, tile_size):
    for j in range(0, len(tiles)):
        for i in range(0, len(tiles[0])):
            if tiles[j][i] == 1:
                colour = (128, 128, 128)
                width = 0
            else:
                pygame.draw.rect(surf, (255, 255, 255), (i * tile_size,
                        j * tile_size, tile_size, tile_size))
                colour = (0, 0, 0)
                width = 1
            pygame.draw.rect(surf, colour, (i * tile_size, j * tile_size,
                    tile_size, tile_size), width)

if __name__ == "__main__": main()
