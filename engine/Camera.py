import numpy as np
import pygame as pg

FAR = 100
NEAR = .1


class Ray:
    def __init__(self, p, d, angle):
        self.p = p  # (2,) numpy array
        self.d = d  # (2,) numpy array
        self.angle = angle


class Camera:
    def __init__(self, screenwidth, screenheight, theta_w, theta_h, near, far, curr_sector, env, recursive):
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False

        self.near = near
        self.far = far

        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.thetaW = np.radians(theta_w)
        self.thetaH = np.radians(theta_h)

        self.c = - self.near / self.far

        self.pos = np.array([75, 3, 75, 1])
        self.heading = 0
        self.look = np.array([np.cos(self.heading), 0, np.sin(self.heading), 0])
        self.eye = self.pos + 1*self.look

        self.translate_mat = np.array([[1, 0, 0, -self.eye[0]],
                                       [0, 1, 0, -self.eye[1]],
                                       [0, 0, 1, -self.eye[2]],
                                       [0, 0, 0, 1]])
        self.w = -np.array([self.look[0], self.look[1], self.look[2]])
        self.v = np.array([0, 1, 0])
        self.u = np.cross(self.v, self.w)
        self.rotate_mat = np.array([[self.u[0], self.u[1], self.u[2], 0],
                                    [self.v[0], self.v[1], self.v[2], 0],
                                    [self.w[0], self.w[1], self.w[2], 0],
                                    [0, 0, 0, 1]])
        self.scale_mat = np.array([[1 / (self.far * np.tan(self.thetaW / 2)), 0, 0, 0],
                                   [0, 1 / (self.far * np.tan(self.thetaH / 2)), 0, 0],
                                   [0, 0, 1 / self.far, 0],
                                   [0, 0, 0, 1]])
        self.perspective_mat = np.array([[1, 0, 0, 0],
                                         [0, 1, 0, 0],
                                         [0, 0, 1 / (1 + self.c), -self.c / (1 + self.c)],
                                         [0, 0, -1, 0]])
        self.view_mat = self.rotate_mat @ self.translate_mat
        self.projection_mat = self.perspective_mat @ self.scale_mat
        self.cumulative_mat = self.projection_mat @ self.view_mat

        a = self.thetaW / 2
        self.left_look = np.array([np.cos(a) * self.look[0] - np.sin(a) * self.look[2],
                                   np.sin(a) * self.look[0] + np.cos(a) * self.look[2]])
        self.right_look = np.array([np.cos(-a) * self.look[0] - np.sin(-a) * self.look[2],
                                    np.sin(-a) * self.look[0] + np.cos(-a) * self.look[2]])

        self.curr_sector = curr_sector
        self.env = env

        self.recursive = recursive

    def processEvents(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.UP = True
                if event.key == pg.K_s:
                    self.DOWN = True
                if event.key == pg.K_a:
                    self.LEFT = True
                if event.key == pg.K_d:
                    self.RIGHT = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.UP = False
                if event.key == pg.K_s:
                    self.DOWN = False
                if event.key == pg.K_a:
                    self.LEFT = False
                if event.key == pg.K_d:
                    self.RIGHT = False

    def update(self, env, transported_camera):
        if self.UP:
            self.pos = self.pos + .5*self.look
        if self.DOWN:
            self.pos = self.pos - .5*self.look
        if self.LEFT:
            self.heading -= .1
            self.look = np.array([np.cos(self.heading), 0, np.sin(self.heading), 0])
        if self.RIGHT:
            self.heading += .1
            self.look = np.array([np.cos(self.heading), 0, np.sin(self.heading), 0])
        self.eye = self.pos - 1 * self.look

        self.translate_mat = np.array([[1, 0, 0, -self.eye[0]],
                                       [0, 1, 0, -self.eye[1]],
                                       [0, 0, 1, -self.eye[2]],
                                       [0, 0, 0, 1]])
        self.w = -np.array([self.look[0], self.look[1], self.look[2]])
        self.v = np.array([0, 1, 0])
        self.u = np.cross(self.v, self.w)
        self.rotate_mat = np.array([[self.u[0], self.u[1], self.u[2], 0],
                                    [self.v[0], self.v[1], self.v[2], 0],
                                    [self.w[0], self.w[1], self.w[2], 0],
                                    [0, 0, 0, 1]])
        self.view_mat = self.rotate_mat @ self.translate_mat
        self.cumulative_mat = self.projection_mat @ self.view_mat
        a = self.thetaW / 2
        self.left_look = np.array([np.cos(a) * self.look[0] - np.sin(a) * self.look[2],
                                   np.sin(a) * self.look[0] + np.cos(a) * self.look[2]])
        self.right_look = np.array([np.cos(-a) * self.look[0] - np.sin(-a) * self.look[2],
                                    np.sin(-a) * self.look[0] + np.cos(-a) * self.look[2]])

        # if we are not the sector we thought we were in, check to see if we are in any of the other sectors
        if not self.recursive and not self.checkInSector(self.curr_sector):
            for sector in self.env.sectors:
                if self.checkInSector(sector):
                    self.curr_sector = sector
                    self.pos[1] = 3 + self.curr_sector.floor_height
                    break

        # go through all the non-euclidean portals in the sector and if we get really close to one, change the position
        # and look vector of this camera
        if not self.recursive and not transported_camera:
            non_euclidean_portals = []
            for wall in self.curr_sector.walls:
                if wall.portal is not None:
                    if wall.portal.center_of_rotation is not None:
                        non_euclidean_portals.append((wall, wall.portal))

            for wall_and_portal in non_euclidean_portals:
                wall = wall_and_portal[0]
                portal = wall_and_portal[1]
                p = np.array([self.pos[0], self.pos[2]])
                possible_t = np.dot(p - wall.p1, wall.p2 - wall.p1) / (np.linalg.norm(wall.p2 - wall.p1) ** 2)
                t = max(0.0, min(1.0, possible_t))
                proj = wall.p1 + t * (wall.p2 - wall.p1)
                dist = np.linalg.norm(proj - p)
                dot = np.dot(np.array([self.look[0], self.look[2]]), wall.normal)
                print(f'dot: {dot}')
                print(f'dist: {dist}')
                if dist < .6 and dot < 0:
                    self.curr_sector = portal.sector
                    self.pos[1] = 3 + self.curr_sector.floor_height
                    look_to_change = np.array([self.look[0], self.look[2]])
                    new_look = portal.rotation_mat @ look_to_change
                    self.look[0] = new_look[0]
                    self.look[2] = new_look[1]
                    pos_to_change = np.array([self.pos[0], self.pos[2]])
                    pos_to_change[0] -= portal.center_of_rotation[0]
                    pos_to_change[1] -= portal.center_of_rotation[1]
                    new_pos = portal.rotation_mat @ pos_to_change
                    pos_to_change[0] = new_pos[0] + portal.new_point[0]
                    pos_to_change[1] = new_pos[1] + portal.new_point[1]
                    self.pos[0] = pos_to_change[0]
                    self.pos[2] = pos_to_change[1]
                    self.pos[1] = portal.new_y + 3
                    self.heading += portal.heading_change
                    self.update(self.env, True)

    def checkInSector(self, sector):
        for wall in sector.walls:
            behind = np.dot(np.array([self.pos[0], self.pos[2]]) - wall.p1, wall.normal) < 0
            if behind:
                return False
        return True


