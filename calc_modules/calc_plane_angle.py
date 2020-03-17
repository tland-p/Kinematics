#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import scipy
'''
calc each plane's angle (only init vec is z vec)
'''
from make_matrix import MakeMatrix

def xy_plane(beofre_R):
    z = np.matrix([[0.],[0.],[1.]])
    rotated = beofre_R * z
    y = rotated[1,0]

    angle_y = math.asin(y)
    deg_y = math.degrees(angle_y)
    print(deg_y)

    return angle_y

def yx_plane(before_R):
    z = np.matrix([[0.], [0.], [1.]])
    rotated = before_R * z
    x = rotated[0,0]

    angle_x = math.asin(x)
    deg_x = math.degrees(angle_x)
    print(deg_x)

    return angle_x

def x_angle(vec):
    x = vec[0,0]
    angle_x = math.asin(x)
    deg_x = math.degrees(x)
    print(deg_x)

    return angle_x


def y_angle(vec):
    y = vec[1, 0]
    angle_y = math.asin(y)
    deg_y = math.degrees(y)
    print(deg_y)

    return angle_y

def quaternion_euler(theta, vec):
    # Rx = np.matrix([[1.0, 0.0, 0.0], [0.0, cos, -sin], [0.0, sin, cos]])
    # Ry = np.matrix([[cos, 0.0, sin], [0.0, 1.0, 0.0], [-sin, 0.0, cos]])

    half_sin = math.sin(theta/2)
    half_cos = math.cos(theta/2)

    # q = [vec[0,0]*half_sin, vec[1,0]*half_sin, vec[2,0]*half_sin, half_cos]
    # print('q',q)
    #
    # Rtheta = np.matrix([[(q[0]*q[0])-(q[1]*q[1])-(q[2]*q[2])+(q[3]*q[3]),2*(q[0]*q[1]-q[2]*q[3]),2*(q[0]*q[2]+q[1]*q[3])],
    #           [2*(q[0]*q[1]+q[2]*q[3]),-(q[0]*q[0])+(q[1]*q[1])-(q[2]*q[2])+(q[3]*q[3]),2*(q[1]*q[2]+q[0]*q[3])],
    #           [2*(q[0]*q[2]-q[1]*q[3]),2*(q[1]*q[2]+q[0]*q[3]),-(q[0]*q[0])-(q[1]*q[1])+(q[2]*q[2])+(q[3]*q[3])]])

    q = [half_cos, vec[0,0]*half_sin, vec[1,0]*half_sin, vec[2,0]*half_sin]
    print('q',q)

    Rtheta = np.matrix([[(q[0]*q[0])+(q[1]*q[1])-(q[2]*q[2])-(q[3]*q[3]),2*(q[1]*q[2]-q[0]*q[3]),2*(q[0]*q[2]+q[1]*q[3])],
              [2*(q[0]*q[3]+q[1]*q[2]),(q[0]*q[0])-(q[1]*q[1])+(q[2]*q[2])-(q[3]*q[3]),2*(-q[0]*q[1]+q[2]*q[3])],
              [2*(q[1]*q[3]-q[0]*q[2]),2*(q[2]*q[3]+q[0]*q[1]),(q[0]*q[0])-(q[1]*q[1])-(q[2]*q[2])+(q[3]*q[3])]])

    tanx = Rtheta[0,1] / Rtheta[0,2]
    tany = Rtheta[0,1] / Rtheta[2,1]

    theta_x = math.atan(tanx)
    theta_y = math.atan(tany)

    theta_x1 = math.atan2(Rtheta[0, 1], Rtheta[0, 2])
    theta_y1 = math.atan2(Rtheta[0, 1], Rtheta[2, 1])

    print('-----')
    print(math.degrees(theta_x), math.degrees(theta_x1))
    print(math.degrees(theta_y), math.degrees(theta_y1))
    print('-----')

    return theta_x1, theta_y1, Rtheta

if __name__ == '__main__':
    # a = np.matrix([[0.5],[0.5],[]])
    z = np.matrix([[0.], [0.], [1.]])
    ang1 = math.radians(30)
    ang2 = math.radians(30)
    mm = MakeMatrix()
    R1x = mm.make_x_matrix(ang1)
    R1y = mm.make_y_matrix(ang1)

    rotated = R1x * R1y * z

