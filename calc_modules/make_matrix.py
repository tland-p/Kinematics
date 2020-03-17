#!/usr/bin/env python
'''
This program make ROTATION MATRIX from ANGLE(rad)

2019.09.09 TORU SHIMAZAKI
'''
import numpy as np
import scipy
import math

class MakeMatrix():

    def make_x_matrix(self, theta):
        cos = math.cos(theta)
        sin = math.sin(theta)

        R = np.matrix([[1.0,0.0,0.0],[0.0,cos,-sin],[0.0,sin,cos]])

        return R

    def make_y_matrix(self, theta):
        cos = math.cos(theta)
        sin = math.sin(theta)

        R = np.matrix([[cos,0.0,sin],[0.0,1.0,0.0],[-sin,0.0,cos]])

        return R

    def make_z_matrix(self, theta):
        cos = math.cos(theta)
        sin = math.sin(theta)

        R = np.matrix([[cos,-sin,0.0],[sin,cos,0.0],[0.0,0.0,1.0]])

        return R

# if __name__ == '__main__':
#     theta = 30
#
#     MM = MakeMatrix()
#     Ax = MM.make_x_matrix(theta)
#     Ay = MM.make_y_matrix(theta)
#     Az = MM.make_z_matrix(theta)
#
#     print(Ax, Ay, Az)