#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import scipy

'''
calc inverse kinematics program from thumb target
THJ3x, THJ2x, THJ2y
'''

def thumb_inverse_kinematics(target,linkvec):
    print('target', target)
    x = target[0,0]
    y = target[1,0]
    z = target[2,0]

    l1 = np.linalg.norm(linkvec[0])
    l2 = np.linalg.norm(linkvec[1])

    S3 = x/l2
    C3 = np.sqrt(1-(S3*S3))
    print('S3=', S3)
    print('C3=', C3)

    theta3 = math.atan2(S3, C3)

    C2 = (((y*y) + (z*z) - (l1*l1) - (C3*C3*l2*l2)) / (2 * C3 * l1 * l2))
    # C2 = -C2
    if C2 > 1.0:
        C2 = 1.0
    elif C2 < -1.0:
        C2 = -1.0
    print('C2=', C2)
    S2 = np.sqrt(1-(C2*C2))
    print('S2=', S2)

    theta2 = math.atan2(S2, C2)

    M = C2*C3*l2+l1
    N = S2*C3*l2

    S1 = ((M*y)+(N*z)) / ((M*(-M))-(N*N))
    print('S1', S1)
    C1 = ((N*y)+(-M*z)) /((M*(-M))-(N*N))
    print('C1', C1)

    theta1 = math.atan2(S1, C1)

    return theta1, theta2, theta3