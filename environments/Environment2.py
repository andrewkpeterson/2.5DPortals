import Renderer
from Sector import Sector
from Wall import Wall
from Wall import Portal
import numpy as np


def makeRotationMat(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])


class Environment2:
    def __init__(self):
        v1 = np.array([0, 0])
        v2 = np.array([40, 0])
        v3 = np.array([100, 0])
        v4 = np.array([20, 10])
        v5 = np.array([40, 10])
        v6 = np.array([40, 40])
        v7 = np.array([60, 40])
        v8 = np.array([80, 40])
        v9 = np.array([100, 40])
        v10 = np.array([40, 60])
        v11 = np.array([60, 60])
        v12 = np.array([80, 60])
        v13 = np.array([100, 60])
        v14 = np.array([0, 90])
        v15 = np.array([20, 90])
        v16 = np.array([40, 90])
        v17 = np.array([100, 90])
        v18 = np.array([0, 100])
        v19 = np.array([100, 100])
        v20 = np.array([140, 0])
        v21 = np.array([160, 0])
        v22 = np.array([140, 80])
        v23 = np.array([160, 80])
        v24 = np.array([110, 0])
        v25 = np.array([130, 0])
        v26 = np.array([110, 20])
        v27 = np.array([130, 20])
        v28 = np.array([0, 10])
        v29 = np.array([20, 100])
        v30 = np.array([40, 100])


        w1 = Wall(v1, v18, 0, 5, None, False, (120, 120, 120))
        w2 = Wall(v18, v19, 0, 5, None, True, (120, 120, 120))
        w3 = Wall(v19, v3, 0, 5, None, True, (120, 120, 120))
        w4 = Wall(v3, v1, 0, 5, None, False, (120, 120, 120))
        s = Sector(0, False, 5, [w1, w2, w3, w4], (0, 0, 0), (0, 0, 0))

        # sector 1
        w1_1 = Wall(v1, v28, 0, 5, None, False, (120, 120, 120))
        p1_2 = Portal(None, 0, 5)
        w1_2 = Wall(v28, v4, 0, 5, p1_2, True, (120, 120, 120))
        p1_3 = Portal(None, 0, 5, center_of_rotation=v4, rotation_mat=np.eye(2), heading_change=0, new_point=v24, new_y=0)
        w1_3 = Wall(v4, v5, 0, 5, p1_3, True, (120, 120, 120))
        p1_4 = Portal(None, 0, 5)
        w1_4 = Wall(v5, v2, 0, 5, p1_4, True, (120, 120, 120))
        w1_5 = Wall(v2, v1, 0, 5, None, False, (120, 120, 120))
        s1 = Sector(0, False, 5, [w1_1, w1_2, w1_3, w1_4, w1_5], (0, 0, 0), (0, 0, 0))

        # sector 2
        p2_1 = Portal(None, 0, 5)
        w2_1 = Wall(v2, v5, 0, 5, p2_1, False, (120, 120, 120))
        w2_2 = Wall(v5, v6, 0, 5, None, False, (120, 120, 120))
        p2_3 = Portal(None, 0, 5)
        w2_3 = Wall(v6, v7, 0, 5, p2_3, True, (120, 120, 120))
        p2_4 = Portal(None, 0, 5)
        w2_4 = Wall(v7, v8, 0, 5, p2_4, True, (120, 120, 120))
        p2_5 = Portal(None, 0, 5)
        w2_5 = Wall(v8, v9, 0, 5, p2_5, True, (120, 120, 120))
        w2_6 = Wall(v9, v3, 0, 5, None, True, (120, 120, 120))
        w2_7 = Wall(v3, v2, 0, 5, None, False, (120, 120, 120))
        s2 = Sector(0, False, 5, [w2_1, w2_2, w2_3, w2_4, w2_5, w2_6, w2_7], (0, 0, 0), (0, 0, 0))

        # sector 3
        w3_1 = Wall(v28, v14, 0, 5, None, False, (120, 120, 120))
        p3_2 = Portal(None, 0, 5)
        w3_2 = Wall(v14, v15, 0, 5, p3_2, True, (120, 120, 120))
        w3_3 = Wall(v15, v4, 0, 5, None, True, (120, 120, 120))
        p3_4 = Portal(None, 0, 5)
        w3_4 = Wall(v4, v28, 0, 5, p3_4, False, (120, 120, 120))
        s3 = Sector(0, False, 5, [w3_1, w3_2, w3_3, w3_4], (0, 0, 0), (0, 0, 0))

        # sector 4
        '''
        w4_1 = Wall(v4, v15, 0, 5, None, False, (120, 120, 120))
        p4_2 = Portal(None, 0, 5, center_of_rotation=v15, rotation_mat=np.eye(2), heading_change=0, new_point=v26, new_y=0)
        w4_2 = Wall(v15, v16, 0, 5, p4_2, True, (120, 120, 120))
        w4_3 = Wall(v16, v5, 0, 5, None, True, (120, 120, 120))
        p4_4 = Portal(None, 0, 5, center_of_rotation=v4, rotation_mat=np.eye(2), heading_change=0, new_point=v24, new_y=0)
        w4_4 = Wall(v5, v4, 0, 5, p4_4, False, (120, 120, 120))
        s4 = Sector(0, False, 5, [w4_1, w4_2, w4_3, w4_4], (0, 0, 0), (0, 0, 0))
        '''

        # sector 5
        w5_1 = Wall(v6, v10, 0, 5, None, False, (120, 120, 120))
        p5_2 = Portal(None, 0, 5)
        w5_2 = Wall(v10, v11, 0, 5, p5_2, True, (120, 120, 120))
        w5_3 = Wall(v11, v7, 0, 5, None, True, (120, 120, 120))
        p5_4 = Portal(None, 0, 5)
        w5_4 = Wall(v7, v6, 0, 5, p5_4, False, (120, 120, 120))
        s5 = Sector(0, False, 5, [w5_1, w5_2, w5_3, w5_4], (0, 0, 0), (0, 0, 0))

        # sector 6
        w6_1 = Wall(v7, v11, 0, 5, None, False, (120, 120, 120))
        p6_2 = Portal(None, 0, 5)
        w6_2 = Wall(v11, v12, 0, 5, p6_2, True, (120, 120, 120))
        w6_3 = Wall(v12, v8, 0, 5, None, True, (120, 120, 120))
        p6_4 = Portal(None, 0, 5)
        w6_4 = Wall(v8, v7, 0, 5, p6_4, False, (120, 120, 120))
        s6 = Sector(0, False, 5, [w6_1, w6_2, w6_3, w6_4], (0, 0, 0), (0, 0, 0))

        # sector 7
        w7_1 = Wall(v8, v12, 0, 5, None, False, (120, 120, 120))
        p7_2 = Portal(None, 0, 5)
        w7_2 = Wall(v12, v13, 0, 5, p7_2, True, (120, 120, 120))
        w7_3 = Wall(v13, v9, 0, 5, None, True, (120, 120, 120))
        p7_4 = Portal(None, 0, 5)
        w7_4 = Wall(v9, v8, 0, 5, p7_4, False, (120, 120, 120))
        s7 = Sector(0, False, 5, [w7_1, w7_2, w7_3, w7_4], (0, 0, 0), (0, 0, 0))

        # sector 8
        w8_1 = Wall(v10, v16, 0, 5, None, False, (120, 120, 120))
        p8_2 = Portal(None, 0, 5)
        w8_2 = Wall(v16, v17, 0, 5, p8_2, True, (120, 120, 120))
        w8_3 = Wall(v17, v13, 0, 5, None, True, (120, 120, 120))
        p8_4 = Portal(None, 0, 5)
        w8_4 = Wall(v13, v12, 0, 5, p8_4, False, (120, 120, 120))
        p8_5 = Portal(None, 0, 5)
        w8_5 = Wall(v12, v11, 0, 5, p8_5, False, (120, 120, 120))
        p8_6 = Portal(None, 0, 5)
        w8_6 = Wall(v11, v10, 0, 5, p8_6, False, (120, 120, 120))
        s8 = Sector(0, False, 5, [w8_1, w8_2, w8_3, w8_4, w8_5, w8_6], (0, 0, 0), (0, 0, 0))

        # sector 9
        w9_1 = Wall(v14, v18, 0, 5, None, False, (120, 120, 120))
        w9_2 = Wall(v30, v19, 0, 5, None, True, (120, 120, 120))
        w9_3 = Wall(v19, v17, 0, 5, None, True, (120, 120, 120))
        p9_4 = Portal(None, 0, 5)
        w9_4 = Wall(v17, v16, 0, 5, p9_4, False, (120, 120, 120))
        s9 = Sector(0, False, 5, [w9_1, w9_2, w9_3, w9_4], (0, 0, 0), (0, 0, 0))
        p9_5 = Portal(None, 0, 5, center_of_rotation=v15, rotation_mat=np.eye(2), heading_change=0, new_point=v26, new_y=0)
        w9_5 = Wall(v16, v15, 0, 5, p9_5, False, (120, 120, 120))
        p9_6 = Portal(None, 0, 5)
        w9_6 = Wall(v15, v14, 0, 5, p9_6, False, (120, 120, 120))

        # sector 10
        w10_1 = Wall(v24, v26, 0, 5, None, False, (150, 0, 0))
        p10_2 = Portal(None, 0, 5, center_of_rotation=v26, rotation_mat=np.eye(2), heading_change=0, new_point=v15, new_y=0)
        w10_2 = Wall(v26, v27, 0, 5, p10_2, True, (120, 120, 120))
        w10_3 = Wall(v27, v25, 0, 5, None, True, (0, 150, 0))
        p10_4 = Portal(None, 0, 5, center_of_rotation=v24, rotation_mat=np.eye(2), heading_change=0, new_point=v4, new_y=0)
        w10_4 = Wall(v25, v24, 0, 5, p10_4, True, (120, 120, 120))
        s10 = Sector(0, False, 5, [w10_1, w10_2, w10_3, w10_4], (0, 0, 0), (0, 0, 0))

        # assign sectors to portals
        p1_2.sector = s3
        p1_3.sector = s10
        p1_4.sector = s5

        p2_1.sector = s1
        p2_3.sector = s5
        p2_4.sector = s6
        p2_5.sector = s7

        p3_2.sector = s9
        p3_4.sector = s1

        #p4_2.sector = s9
        #p4_4.sector = s1

        p5_2.sector = s8
        p5_4.sector = s2

        p6_2.sector = s8
        p6_4.sector = s2

        p7_2.sector = s8
        p7_4.sector = s2

        p8_2.sector = s9
        p8_4.sector = s7
        p8_5.sector = s6
        p8_6.sector = s5

        p9_4.sector = s8
        p9_5.sector = s10
        p9_6.sector = s3

        p10_2.sector = s9
        p10_4.sector = s1

        self.sectors = [s1, s2, s3, s5, s6, s7, s8, s9, s10]




