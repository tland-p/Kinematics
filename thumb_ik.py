#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import scipy
import time

from calc_modules.thumb_inverse_kinematics import thumb_inverse_kinematics
from calc_modules.make_matrix import MakeMatrix
from forward_kinematics import ForwardKinematics
from data_import import data_tp

if __name__ == '__main__':
    start = time.time()
    # Forward Kinematics (target is fk_position[1]), and link_vec use link_vec[0] and link_vec[1]
    data = data_tp()
    # print(data)
    '''
    1 = 原点
    2 = スタイラス
    3 = 手の甲
    4 = x
    5 = x
    6 = 第一中手骨
    7 = 基節骨
    8 = 末節骨
    '''
    base = []
    endpoint = []
    print(len(data))
    count = 0
    for i in data:
        print(count)
        print(data[count,1])
        if data[count,1] == str('01'):
            base.append([data[count,3],data[count,4],data[count,5],data[count,6],data[count,7],data[count,8]])

        elif data[count,2] == '08':
            endpoint.append([data[count,3],data[count,4],data[count,5],data[count,6],data[count,7],data[count,8]])
        count += 1

    print(base,endpoint)

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

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print(target, endpoint)
    print(np.linalg.norm(target), np.linalg.norm(endpoint))

