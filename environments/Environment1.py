import Renderer
from Sector import Sector
from Wall import Wall
from Wall import Portal
import numpy as np


def makeRotationMat(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])


class Environment1:
    def __init__(self):
        ne_portal1 = Portal(None, 0, 5, np.array([50, 50]), makeRotationMat(np.radians(45)), 45, np.array([135, 100]), 0)
        opening_portal1 = Portal(None, 1, 5)

        # make first sector
        vec1 = np.array([50, 50])
        vec2 = np.array([25, 75])
        vec3 = np.array([100, 100])

        wall1 = Wall(vec1, vec2, 0, 6, ne_portal1, False, (150, 0, 0))
        wall2 = Wall(vec2, vec3, 0, 6, None, False, (150, 0, 150))
        wall3 = Wall(vec3, vec1, 0, 6, opening_portal1, True, (150, 0, 150))
        sector1 = Sector(1, True, 5, [wall3, wall2, wall1], (100, 0, 100), (100,100,0))

        # make second sector
        vec1 = np.array([50, 50])
        vec2 = np.array([100, 100])
        vec3 = np.array([135, 100])
        vec4 = np.array([200, 50])
        vec5 = np.array([75, 25])

        opening_portal2 = Portal(sector1, 1, 5)
        ne_portal2 = Portal(sector1, 1, 4, np.array([135, 100]), makeRotationMat(np.radians(-45)), -45, np.array([50, 50]), 1)

        wall1 = Wall(vec1, vec2, 0, 5, opening_portal2, False, (150, 0, 0))
        wall2 = Wall(vec2, vec3, 0, 5, ne_portal2, True, (150, 0, 150))
        wall3 = Wall(vec3, vec4, 0, 5, None, True, (150, 150, 0))
        wall4 = Wall(vec4, vec5, 0, 5, None, True, (150, 150, 150))
        wall5 = Wall(vec5, vec1, 0, 5, None, False, (150, 150, 150))
        sector2 = Sector(0, True, 5, [wall2, wall1, wall3, wall4, wall5], (100, 100, 100), (100,0 ,100))

        ne_portal1.sector = sector2
        opening_portal1.sector = sector2

        self.sectors = [sector1, sector2]  # an environment is a list of sectors