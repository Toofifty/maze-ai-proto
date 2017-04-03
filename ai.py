import time, pygame
from util import draw_box, is_empty

class Node(object):
    def __init__(self, x, y, wall):
        self.x = x
        self.y = y
        self.wall = wall
        self.adj = [None] * 4
        self.num_adj = 0

    def is_at(self, x, y):
        return self.x == x and self.y == y

    def add_adjs(self, nodes):
        self.add_adj(0, get_node(nodes, self.x, self.y - 1))
        self.add_adj(1, get_node(nodes, self.x + 1, self.y))
        self.add_adj(2, get_node(nodes, self.x, self.y + 1))
        self.add_adj(3, get_node(nodes, self.x - 1, self.y))
        self.num_adj = sum([1 for adj in self.adj
            if adj is not None and not adj.wall])

    def add_adj(self, d, node):
        self.adj[d] = node

    def begin_search(self, players):
        searches = [999] * 4
        for n in range(0, 4):
            try:
                searches[n] = self.adj[n].search([], (n-2) % 4, 1, players)
            except AttributeError:
                print "Node in dir", n, "not found"
        return searches.index(min(searches))

    def search(self, searched, from_dir, dist, players):
        if self.num_adj > 2:
            if [self.x, self.y] in searched:
                return 999
            searched.append([self.x, self.y])
        if self.wall or dist > 100:
            return 999
        for player in players:
            if self.is_at(player.x, player.y):
                return dist
        searches = [999] * 4
        for n in range(0, 4):
            if not n == from_dir:
                try:
                    searches[n] = self.adj[n].search(searched[:], (n-2) % 4,
                            dist + 1, players)
                except AttributeError:
                    print "Node in dir", n, "not found"

        mins = min(searches)
        if mins != 999:
            draw_box(self.x, self.y, (255, (dist * 32) % 255, 255))
        return mins

def init(size):
    nodes = []
    # create nodes
    for j in range(0, size):
        for i in range(0, size):
            nodes.append(Node(i, j, not is_empty(i, j)))
    # add adjs
    for j in range(0, size):
        for i in range(0, size):
            nodes[j * size + i].add_adjs(nodes)
    return nodes

def get_node(nodes, x, y):
    for node in nodes:
        if node.is_at(x, y):
            return node
    return None

def ai_step(framecount, nodes, monster, players):
    current_node = get_node(nodes, monster.x, monster.y)
    d = current_node.begin_search(players)
    if framecount % 10 == 0:
        print "moving:", d
        if d == 0:
            monster.add_pos(0, -1)

        elif d == 1:
            monster.add_pos(1, 0)

        elif d == 2:
            monster.add_pos(0, 1)

        elif d == 3:
            monster.add_pos(-1, 0)
