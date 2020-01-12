import Renderer
from Sector import Sector
from Wall import Wall
from Wall import Portal
import numpy as np


def makeRotationMat(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])


class Environment3:
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
        v24 = np.array([150, 10])
        v25 = np.array([170, 20])
        v26 = np.array([150, 70])
        v27 = np.array([170, 60])
        v28 = np.array([0, 10])
        v29 = np.array([20, 100])
        v30 = np.array([40, 100])
        v31 = np.array([100, 10])
        v32 = np.array([145, 10])
        v33 = np.array([190, 10])
        v34 = np.array([145, 70])
        v35 = np.array([190, 70])
        v36 = np.array([50, 10])
        v37 = np.array([50, 90])
        v38 = np.array([20, 0])
        v39 = np.array([50, 0])
        v40 = np.array([50, 100])
        v41 = np.array([20, 50])
        v42 = np.array([40, 50])
        v43 = np.array([150, 20])
        v44 = np.array([150, 60])
        v45 = np.array([40, 20])


        p = Portal(None, 0, 5)

        # sector 1
        w1_1 = Wall(v39, v36, 0, 5, p, False, (120, 120, 120))
        w1_3 = Wall(v36, v37, 0, 5, None, False, (120, 120, 120))
        w1_4 = Wall(v37, v40, 0, 5, p, False, (120, 120, 120))
        w1_5 = Wall(v40, v19, 0, 5, None, True, (0, 150, 0))
        w1_6 = Wall(v19, v3, 0, 5, None, True, (120, 120, 120))
        w1_7 = Wall(v3, v39, 0, 5, None, False, (150, 0, 0))
        s1 = Sector(0, False, 5, [w1_1, w1_3, w1_4, w1_5, w1_6, w1_7], (0, 0, 0), (0, 0, 0), "1")

        # sector 3
        w3_1 = Wall(v38, v4, 0, 5, None, False, (120, 120, 120))
        p3_2 = Portal(None, 0, 5, center_of_rotation=v4, rotation_mat=np.eye(2), heading_change=0, new_point=v24,
                      new_y=0)
        w3_2 = Wall(v4, v5, 0, 5, p3_2, True, (120, 120, 120))
        w3_3 = Wall(v5, v36, 0, 5, None, True, (120, 120, 120))
        w3_4 = Wall(v36, v39, 0, 5, p, True, (120, 120, 120))
        w3_5 = Wall(v39, v38, 0, 5, None, False, (150, 0, 0))
        #w3_6 = Wall(v6, v45, 0, 5, None, True, (120, 120, 120))
        s3 = Sector(0, False, 5, [w3_1, w3_2, w3_3, w3_4, w3_5], (0, 0, 0), (0, 0, 0), "3")

        # sector 4
        w4_1 = Wall(v15, v29, 0, 5, None, False, (120, 120, 120))
        w4_2 = Wall(v29, v40, 0, 5, None, True, (0, 150, 0))
        w4_3 = Wall(v40, v37, 0, 5, p, True, (120, 120, 120))
        w4_4 = Wall(v37, v16, 0, 5, None, False, (120, 120, 120))
        p4_4 = Portal(None, 0, 5, center_of_rotation=v15, rotation_mat=np.eye(2), heading_change=0, new_point=v26,
                      new_y=0)
        w4_5 = Wall(v16, v15, 0, 5, p4_4, False, (120, 120, 120))
        s4 = Sector(0, False, 5, [w4_1, w4_2, w4_3, w4_4, w4_5], (0, 0, 0), (0, 0, 0), "4")

        # sector 6

        w6_1 = Wall(v38, v29, 0, 5, None, False, (120, 120, 120))
        w6_2 = Wall(v15, v16, 0, 5, p, True, (120, 120, 120))
        w6_3 = Wall(v16, v5, 0, 5, p, True, (120, 120, 120))
        w6_4 = Wall(v5, v4, 0, 5, p, False, (120, 120, 120))
        s6 = Sector(0, False, 5, [w6_1, w6_2, w6_3, w6_4], (0, 0, 0), (0, 0, 0), "6")


        # sector 10
        w10_1 = Wall(v24, v26, 0, 5, None, False, (120, 120, 120))
        p10_2 = Portal(None, 0, 5, center_of_rotation=v44, rotation_mat=np.eye(2), heading_change=0, new_point=v15, new_y=0)
        w10_2 = Wall(v44, v27, 0, 5, p10_2, True, (120, 120, 120))
        w10_3 = Wall(v27, v25, 0, 5, None, True, (120, 120, 120))
        p10_4 = Portal(None, 0, 5, center_of_rotation=v43, rotation_mat=np.eye(2), heading_change=0, new_point=v4, new_y=0)
        w10_4 = Wall(v25, v43, 0, 5, p10_4, False, (120, 120, 120))
        w10_5 = Wall(v33, v32, 0, 5, None, False, (150, 0, 0))
        w10_6 = Wall(v34, v35, 0, 5, None, True, (0, 150, 0))

        s10 = Sector(0, False, 5, [w10_5, w10_6, w10_1, w10_2, w10_3, w10_4], (0, 0, 0), (0, 0, 0), "10")

        # set portal sectors
        p3_2.sector = s10
        p4_4.sector = s10
        p10_2.sector = s4
        p10_4.sector = s1

        self.sectors = [s1, s3, s4, s6, s10]


