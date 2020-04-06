#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import scipy

from calc_modules.thumb_inverse_kinematics import thumb_inverse_kinematics
from calc_modules.make_matrix import MakeMatrix
from forward_kinematics import ForwardKinematics
from data_import import

if __name__ == '__main__':
    # Forward Kinematics (target is fk_position[1]), and link_vec use link_vec[0] and link_vec[1]
    fk = ForwardKinematics()
    link_vec, fk_position, fk_main_vec, fk_sub_xvec, fk_sub_yvec = fk.forward_kinematics()
    link_vec.pop()
    print(link_vec, fk_position)
    target = fk_position[1]

    # calc Inverse Kinematics (theta1 and theta2 = axis_x, theta3 = axis_y
    theta1, theta2, theta3 = thumb_inverse_kinematics(target, link_vec)

    mm = MakeMatrix()
    print(math.degrees(theta1), math.degrees(theta2), math.degrees(theta3))
    R1 = mm.make_x_matrix(theta1)
    R2 = mm.make_x_matrix(theta2)
    R3 = mm.make_y_matrix(theta3)
    l1 = link_vec[0]
    l2 = link_vec[1]

    endpoint = R1 * (l1 + R2 * R3 * l2)

    print(target, endpoint)
    print(np.linalg.norm(target), np.linalg.norm(endpoint))

