#!usr/bin/env python
# -*- coding:utf-8 -*-
'''
このプログラムのpositionはベースポジション np.matrix([[0.],[0.],[0.]]) がないので注意
'''
import math
import scipy
import numpy as np

from calc_modules.make_matrix import MakeMatrix
from calc_modules.make_linkvec import make_linkvec
from data.joint_angles import JointAngles
from data.joint_positions import JointPositions
from previous_endpoint import previous_endpoint

class ForwardKinematics:

    def forward_kinematics(self):
        mm = MakeMatrix()
        ang = JointAngles()
        pos = JointPositions()

        linkvec = make_linkvec(pos.THJ_sets_pos)
        angles = ang.THJ_SET_RAD

        R = []

        main_vec = np.matrix([[0.], [0.], [1.]])
        sub_xvec = np.matrix([[1.], [0.], [0.]])
        sub_yvec = np.matrix([[0.], [1.], [0.]])

        # Thumb
        for i in xrange(len(angles)):
            if i == 0:
                R.append(mm.make_z_matrix(angles[i]))

            elif i <= 2:
                R.append(mm.make_x_matrix(angles[i]))

            else:
                R.append(mm.make_y_matrix(angles[i]))
                
        fk_position = []
        fk_main_vec = []
        fk_sub_xvec = []
        fk_sub_yvec = []

        fk_position.append(R[0] * R[1] * linkvec[0])     # THJ1
        fk_position.append(R[0] * R[1] * (linkvec[0] + R[2] * R[3] * linkvec[1]))    # THJ2
        fk_position.append(R[0] * R[1] * (linkvec[0] + R[2] * R[3] * (linkvec[1] + R[4] * linkvec[2]))) # THJ3

        rotation = np.matrix([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
        for i in xrange(len(R)):
            rotation = rotation * R[i]
            if i == 0 or i == 2:
                continue

            fk_main_vec.append(rotation*main_vec)
            fk_sub_xvec.append(rotation*sub_xvec)
            fk_sub_yvec.append(rotation*sub_yvec)

        # print(R[0]*R[1]*R[2]*R[3]*R[4]*main_vec)
        # print(np.linalg.norm(fk_main_vec[2]))

        ###
        before_pos = previous_endpoint(fk_position[2], linkvec[2], fk_main_vec[2])
        # print(before_pos)
        # print(fk_position[1])

        return linkvec, fk_position, fk_main_vec, fk_sub_xvec, fk_sub_yvec
        # # other
        # for i in xrange(len(angles)):
        #     if i == 0:
        #         R.append(mm.make_y_matrix(angles[i]))
        #         
        #     else:
        #         R.append(mm.make_x_matrix(angles[i]))

# if __name__ == '__main__':
#     fk = ForwardKinematics()
#     a,b,c,d,e = fk.forward_kinematics()