#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import scipy

from make_matrix import MakeMatrix

def calc_prevoius_pos(target, posture):

if __name__ == '__main__':
    posture_x = np.matrix([[1.], [0.], [0.]])
    posture_y = np.matrix([[0.], [1.], [0.]])
    posture_z = np.matrix([[0.], [0.], [1.]])

    posture = np.matrix([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])

    theta_x = math.radians(30)
    theta_y = math.radians(60)
    theta_z = math.radians(45)

    vec = np.matrix([[0.],[0.],[10.]])
    mm = MakeMatrix()

    Rx = mm.make_x_matrix(theta_x)
    Ry = mm.make_y_matrix(theta_y)
    Rz = mm.make_z_matrix(theta_z)

