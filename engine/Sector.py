import numpy as np

class Sector:
    """A convex collection of walls with a single floor and ceiling height"""
    def __init__(self, floor_height, has_ceiling, ceiling_height, walls, ceiling_color, floor_color, name, extra_walls=None):
        self.floor_height = floor_height
        self.ceiling_height = ceiling_height
        self.walls = walls
        self.ceiling_color = ceiling_color
        self.floor_color = floor_color
        self.name = name
        self.extra_walls = extra_walls

        total = np.array([0.0, 0.0])
        for wall in self.walls:
            total += (wall.p1 + wall.p2) / 2
        self.center = total / len(walls)
