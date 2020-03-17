#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np

class JointPositions:
    def __init__(self):
        sin45 = math.sin(math.radians(45))
        print(sin45)

        P_WRJ2 = np.matrix([[0.0], [0.0], [0.0]])
        P_WRJ1 = np.matrix([[0.0], [0.0], [20.0]])

        P_THJ3 = np.matrix([[41.01 * sin45 + 5.0], [0.0], [20.0 + 41.01 * sin45]])
        P_THJ2 = np.matrix([[79.01 * sin45 + 5.0], [0.0], [20.0 + 79.01 * sin45]])
        P_THJ1 = np.matrix([[111.01 * sin45 + 5.0], [0.0], [20.0 + 111.01 * sin45]])
        P_THJ0 = np.matrix([[138.51 * sin45 + 5.0], [0.0], [20.0 + 138.51 * sin45]])

        # リンクベクトルとしてz軸にまっすぐ親指を伸ばしたと考える．
        # P_THJ3 = np.matrix([[0.], [0.], [41.01]])
        # P_THJ2 = np.matrix([[0.], [0.], [79.01]])
        # P_THJ1 = np.matrix([[0.], [0.], [111.01]])
        # P_THJ0 = np.matrix([[0.], [0.], [138.51]])


        P_THJ3 = np.matrix([[0.], [0.], [0]])
        P_THJ2 = np.matrix([[0.], [0.], [38.0]])
        P_THJ1 = np.matrix([[0.], [0.], [70.0]])
        P_THJ0 = np.matrix([[0.], [0.], [97.5]])

        self.THJ_sets_pos = [P_THJ3, P_THJ2, P_THJ1, P_THJ0]
        self.WRJ_THJ_sets_pos = [P_WRJ1, self.THJ_sets_pos]

        self.test = []
        for i in xrange(len(self.THJ_sets_pos)):
            print(np.linalg.norm(self.THJ_sets_pos[i]))
            self.test.append(np.matrix([[0.],[0.],[i*20.]]))

# if __name__ == '__main__':
#     pos = JointPositions()
#
#     print(pos.THJ_sets_pos)
#     print(pos.WRJ_THJ_sets_pos)