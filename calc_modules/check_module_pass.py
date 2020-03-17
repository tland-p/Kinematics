#!usr/bin/env python
# -*- coding:utf-8 -*-
from make_matrix import MakeMatrix
from ..data.joint_angles import JointAngles
from ..data.joint_positions import JointPositions

def check_module():
    theta = 60
    MM = MakeMatrix()
    A = MM.make_x_matrix(theta)

    print(A)

def check_datas():
    angles = JointAngles()
    positions = JointPositions()

    print(angles.THJ_SET_RAD)
    print(positions.THJ_sets_pos)

if __name__ == '__main__':
    a = check_module()
    b = check_datas()
    print('ok')