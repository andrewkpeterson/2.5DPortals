import numpy as np


class Portal:
    def __init__(self, sector, y, height, center_of_rotation=None, rotation_mat=None, heading_change=None, new_point=None, new_y=None):
        self.sector = sector
        self.y = y
        self.height = height
        self.center_of_rotation = center_of_rotation
        self.rotation_mat = rotation_mat
        self.new_point = new_point
        self.heading_change = heading_change
        self.new_y = new_y


class WallSegment:
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4


'''
A wall can consist of a single segment, a portal, a portal with one segment above or below, and a portal with a segment 
above and below. The portal takes up the entire span of the wall along its line in the x-z plane.
'''
class Wall:
    def __init__(self, p1, p2, y, height, portal, reverse_normal, color):
        self.color = color
        self.p1 = p1  # (2,) numpy array
        self.p2 = p2  # (2,) numpy array
        self.d = p2 - p1
        self.y = y  # must be same as the floor_height of the sector this wall belongs to
        self.height = height

        self.portal = portal
        self.segments = []
        if portal is None:
            v1 = np.array([p1[0], y, p1[1], 1])
            v2 = np.array([p1[0], y + height, p1[1], 1])
            v3 = np.array([p2[0], y + height, p2[1], 1])
            v4 = np.array([p2[0], y, p2[1], 1])
            self.segments.append((WallSegment(v1, v2, v3, v4), 'entire'))
        else:
            seg_below = False
            seg_above = False
            if portal.y < self.y:
                print('invalid portal')
            elif portal.y > self.y:
                seg_below = True

            if portal.y + portal.height > self.y + self.height:
                print('invalid portal')
            elif portal.y + portal.height < self.y + self.height:
                seg_above = True

            if seg_below:
                v1 = np.array([p1[0], y, p1[1], 1])
                v2 = np.array([p1[0], y + portal.y, p1[1], 1])
                v3 = np.array([p2[0], y + portal.y, p2[1], 1])
                v4 = np.array([p2[0], y, p2[1], 1])
                self.segments.append((WallSegment(v1, v2, v3, v4), 'bottom'))

            if seg_above:
                v1 = np.array([p1[0], portal.y + portal.height, p1[1], 1])
                v2 = np.array([p1[0], y + height, p1[1], 1])
                v3 = np.array([p2[0], y + height, p2[1], 1])
                v4 = np.array([p2[0], portal.y + portal.height, p2[1], 1])
                self.segments.append((WallSegment(v1, v2, v3, v4), 'top'))

        # calculate normal vector to the wall
        p = p1 - p2
        if p[0] != 0:
            slope = p[1] / p[0]
            if slope == 0:
                self.normal = np.array([0, 1])
            else:
                self.normal = np.array([1, -1/slope]) / np.linalg.norm([1, -1/slope])
        else:
            self.normal = np.array([1, 0])
        if reverse_normal:
            self.normal = -self.normal

