import pygame as pg
import numpy as np
from Camera import Camera


class Renderer:

    def __init__(self):
        self.sectors_rendered = []

    def sortPortals(self, camera, portals):
        distances = []
        for portal in portals:
            distances.append(self.dist(portal.sector.center, np.array([camera.pos[0], camera.pos[2]])))
        permutation = sorted(range(len(distances)), key=lambda k: distances[k], reverse=True)
        sorted_portals = []
        for i in permutation:
            sorted_portals.append(portals[i])
        return sorted_portals

    def sortSectors(self, camera, env):
        distances = []
        for sector in env.sectors:
            distances.append(self.dist(sector.center, np.array([camera.pos[0], camera.pos[2]])))
        permutation = sorted(range(len(distances)), key=lambda k: distances[k], reverse=True)
        sorted_sectors = []
        for i in permutation:
            sorted_sectors.append(env.sectors[i])
        return sorted_sectors

    def cross2D(self, vec1, vec2):
        return vec1[0] * vec2[1] - vec1[1] * vec2[0]

    def dist(self, vec1, vec2):
        return np.linalg.norm(vec1 - vec2)

    def checkForIntersection(self, pos, ray_dir, wall, right, behind):
        # represent wall as p_wall + d_wall*s where 0 < s <1
        p_wall = wall.p2
        p_dir = wall.p1 - wall.p2

        cross = self.cross2D(ray_dir, p_dir)

        t = self.cross2D(p_wall - pos, p_dir) / cross
        u = self.cross2D(p_wall - pos, ray_dir) / cross
        # increase the area around which we declare an intersection slightly. This helps when the you get very close to the wall.
        if -.05 <= u <= 1.05 and t >= 0:
            if right:
                # slide the point of intersection along the wall slightly so that the line along which the wall is clipped is always off screen
                u = u - .05
            else:
                # slide the point of intersection along the wall slightly so that the line along which the wall is clipped is always off screen
                u = u + .05
            return True, t, p_wall + u * p_dir
        else:
            return False, None, None

    def NDC2Screen(self, camera, vertex):
        return np.array([(.5 + .5 * vertex[0]) * camera.screenwidth, -(.5 + .5 * vertex[1]) * camera.screenheight + camera.screenheight])

    def renderWallSegment(self, screen, camera, wall, segment, sector):
        seg = segment[0]
        transformed_vert1 = camera.cumulative_mat @ seg.v1
        transformed_vert2 = camera.cumulative_mat @ seg.v2
        transformed_vert3 = camera.cumulative_mat @ seg.v3
        transformed_vert4 = camera.cumulative_mat @ seg.v4

        # we need to take the difference between the current camera position and any point on the line segment
        behind = np.dot(np.array([camera.pos[0], camera.pos[2]]) - wall.p1, wall.normal) < 0

        if not behind:
            right_intersection = True
            left_intersection = True
            if not (-abs(transformed_vert1[3]) <= transformed_vert1[0] <= abs(transformed_vert1[3])) or \
               not (-abs(transformed_vert1[3]) <= transformed_vert1[2] <= abs(transformed_vert1[3])):
                left_intersection, _, point = self.checkForIntersection(np.array([camera.pos[0], camera.pos[2]]),
                                                                   np.array([camera.left_look[0], camera.left_look[1]]), wall, False, behind)
                if point is not None:
                    transformed_vert1 = np.copy(seg.v1).astype(np.float32)
                    transformed_vert1[0] = point[0]
                    transformed_vert1[2] = point[1]
                    transformed_vert1 = camera.cumulative_mat @ transformed_vert1
                    transformed_vert2 = np.copy(seg.v2).astype(np.float32)
                    transformed_vert2[0] = point[0]
                    transformed_vert2[2] = point[1]
                    transformed_vert2 = camera.cumulative_mat @ transformed_vert2
                    pg.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 3, 3)

            if not (-abs(transformed_vert4[3]) <= transformed_vert4[0] <= abs(transformed_vert4[3])) or \
               not (-abs(transformed_vert4[3]) <= transformed_vert4[2] <= abs(transformed_vert4[3])):
                right_intersection, _, point = self.checkForIntersection(np.array([camera.pos[0], camera.pos[2]]),
                                                                    np.array([camera.right_look[0], camera.right_look[1]]), wall, True, behind)
                if point is not None:
                    transformed_vert3 = np.copy(seg.v3).astype(np.float32)
                    transformed_vert3[0] = point[0]
                    transformed_vert3[2] = point[1]
                    transformed_vert3 = camera.cumulative_mat @ transformed_vert3
                    transformed_vert4 = np.copy(seg.v4).astype(np.float32)
                    transformed_vert4[0] = point[0]
                    transformed_vert4[2] = point[1]
                    transformed_vert4 = camera.cumulative_mat @ transformed_vert4
                    pg.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 3, 3)

            if not (not right_intersection and not left_intersection):
                transformed_vert1 /= transformed_vert1[3]
                transformed_vert2 /= transformed_vert2[3]
                transformed_vert3 /= transformed_vert3[3]
                transformed_vert4 /= transformed_vert4[3]

                v1 = self.NDC2Screen(camera, transformed_vert1)
                v2 = self.NDC2Screen(camera, transformed_vert2)
                v3 = self.NDC2Screen(camera, transformed_vert3)
                v4 = self.NDC2Screen(camera, transformed_vert4)

                # this only works if the up vector is always [0, 1, 0]
                top_slope = (v2[1] - v3[1]) / (v2[0] - v3[0])
                bottom_slope = (v1[1] - v4[1]) / (v1[0] - v4[0])
                for x in range(int(v4[0]), int(v1[0])):
                    #if segment[1] == 'entire' or segment[1] == 'top':
                        #pg.draw.line(screen, sector.ceiling_color,
                                     #(x, 0), (x, v1[1] + bottom_slope * (x - v1[0])), 1)
                    '''
                    if segment[1] == 'entire':
                        c = (255, 0 ,0)
                    elif segment[1] == 'bottom':
                        c = (0, 255, 0)
                    elif segment[1] == 'top':
                        c = (0, 0, 255)
                    '''
                    pg.draw.line(screen, wall.color, (x, v1[1] + bottom_slope * (x - v1[0])), (x, v2[1] + top_slope * (x - v2[0])), 1)
                    #if segment[1] == 'entire' or segment[1] == 'bottom':
                        #pg.draw.line(screen, sector.floor_color,
                                     #(x, v1[1] + bottom_slope * (x - v1[0])), (x, camera.screenheight), 1)

                pg.draw.polygon(screen, (0, 0, 0), [(v1[0], v1[1]), (v2[0], v2[1]), (v3[0], v3[1]), (v4[0], v4[1])], True)

    def renderWall(self, screen, camera, wall, sector):
        for segment in wall.segments:
            self.renderWallSegment(screen, camera, wall, segment, sector)

    def renderPortal(self, screen, camera, portal, recursions):
        # render the sector that we can see through the portal
        if recursions < 1:
            # render an opening portal by going through
            new_camera = Camera(camera.screenwidth, camera.screenheight, np.degrees(camera.thetaW), np.degrees(camera.thetaH),
                                camera.near, camera.far, camera.curr_sector, camera.env, True)
            new_camera.look = np.copy(camera.look)
            new_camera.pos = np.copy(camera.pos)

            look_to_change = np.array([new_camera.look[0], new_camera.look[2]])
            new_look = portal.rotation_mat @ look_to_change
            new_camera.look[0] = new_look[0]
            new_camera.look[2] = new_look[1]
            pos_to_change = np.array([new_camera.pos[0], new_camera.pos[2]])
            pos_to_change[0] -= portal.center_of_rotation[0]
            pos_to_change[1] -= portal.center_of_rotation[1]
            new_pos = portal.rotation_mat @ pos_to_change
            pos_to_change[0] = new_pos[0] + portal.new_point[0]
            pos_to_change[1] = new_pos[1] + portal.new_point[1]
            new_camera.pos[0] = pos_to_change[0]
            new_camera.pos[2] = pos_to_change[1]
            new_camera.update(camera.env, False)
            self.renderSector(screen, new_camera, portal.sector, True, recursions + 1)

            if not camera.recursive:
                cam_color = (0, 255, 0)
            else:
                cam_color = (255, 0, 0)
            pg.draw.circle(screen, cam_color, (int(camera.eye[0]), int(camera.eye[2])), 5, 2)
            a = camera.thetaW / 2
            left_look = (np.cos(a) * camera.look[0] - np.sin(a) * camera.look[2], np.sin(a) * camera.look[0] + np.cos(a) * camera.look[2])
            right_look = (np.cos(-a) * camera.look[0] - np.sin(-a) * camera.look[2],
                          np.sin(-a) * camera.look[0] + np.cos(-a) * camera.look[2])
            pg.draw.line(screen, (0, 0, 0), (int(camera.eye[0]), int(camera.eye[2])),
                         (int(camera.eye[0] + 50 * left_look[0]), int(camera.eye[2] + 50 * left_look[1])), 1)
            pg.draw.line(screen, (0, 0, 0), (int(camera.eye[0]), int(camera.eye[2])),
                         (int(camera.eye[0] + 50 * right_look[0]), int(camera.eye[2] + 50 * right_look[1])), 1)

    def renderSector(self, screen, camera, sector, recursive, recursions):

        #if (sector not in self.sectors_rendered and camera.recursive) or not camera.recursive:
        if recursive:
            portals = []
            for wall in sector.walls:
                if wall.portal is not None and wall.portal.center_of_rotation is not None:
                    portals.append(wall.portal)
            portals = self.sortPortals(camera, portals)
            if len(portals) > 0:
                print('rendering recursively')
            for portal in portals:
                self.renderPortal(screen, camera, portal, recursions)

        for wall in sector.walls:
            self.renderWall(screen, camera, wall, sector)

    def renderEnvironment(self, screen, camera, env):
        sorted_sectors = self.sortSectors(camera, env)
        for sector in sorted_sectors:
            self.renderSector(screen, camera, sector, False, 0)
        # render the sectors relevant to the portals in the current sector if they exist

        self.renderSector(screen, camera, camera.curr_sector, False, 0)
        portals = []
        for wall in camera.curr_sector.walls:
            if wall.portal is not None and wall.portal.center_of_rotation is not None:
                portals.append(wall.portal)
                print('found_portal')
        portals = self.sortPortals(camera, portals)
        for portal in portals:
            self.renderPortal(screen, camera, portal, 0)

        self.renderSector(screen, camera, camera.curr_sector, False, 0)


    def renderFrame(self, screen, camera, env):
        self.sectors_rendered = []
        screen.fill((255, 255, 255))
        self.renderEnvironment(screen, camera, env)
        print(camera.curr_sector.name)
        # draw map and camera
        for sector in env.sectors:
            for wall in sector.walls:
                pg.draw.line(screen, (0, 0, 0), wall.p1, wall.p2, 1)
                '''
                pg.draw.line(screen, (0, 0, 0), (wall.p1 + wall.p2) / 2, (((wall.p1 + wall.p2) / 2)[0] + 20 * wall.normal[0],
                                                                          ((wall.p1 + wall.p2) / 2)[1] + 20 * wall.normal[1]), 1)
                '''

        pg.draw.circle(screen, (0,255,0), (int(camera.eye[0]), int(camera.eye[2])), 5, 2)
        a = camera.thetaW / 2
        left_look = (
        np.cos(a) * camera.look[0] - np.sin(a) * camera.look[2], np.sin(a) * camera.look[0] + np.cos(a) * camera.look[2])
        right_look = (np.cos(-a) * camera.look[0] - np.sin(-a) * camera.look[2],
                      np.sin(-a) * camera.look[0] + np.cos(-a) * camera.look[2])
        pg.draw.line(screen, (0, 0, 0), (int(camera.eye[0]), int(camera.eye[2])),
                     (int(camera.eye[0] + 50 * left_look[0]), int(camera.eye[2] + 50 * left_look[1])), 1)
        pg.draw.line(screen, (0, 0, 0), (int(camera.eye[0]), int(camera.eye[2])),
                     (int(camera.eye[0] + 50 * right_look[0]), int(camera.eye[2] + 50 * right_look[1])), 1)



