#!usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import scipy
import math
from make_matrix import MakeMatrix

class CalcAngle:
    def __init__(self):
        pass

    def rotation_to_zvec(self, vec):
        length = np.linalg.norm(vec)
        zvec =  np.matrix([[0.],[0.],[length]])
        # t_vec = vec.T
        # list_vec = t_vec.tolist()
        # list = []
        # list.extend(list_vec[0])

        print(x,y,z)

    def calc_cross(self, vec1, vec2):
        A = np.array([vec1[0,0], vec1[1,0], vec1[2,0]])
        B = np.array([vec2[0,0], vec2[1,0], vec2[2,0]])

        outer = np.cross(A, B)
        outer_matrix = np.matrix([[outer[0]], [outer[1]], [outer[2]]])

        # print(A,B, type(A))
        # print(outer, type(outer))
        # print(outer_matrix, type(outer_matrix))

        return outer_matrix

    def calc_corner(self, vec1, vec2):
        dot = vec1.T * vec2
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)

        cos = dot / (norm1 * norm2)
        theta = math.acos(cos)

        return theta

    def rodrigues_rotation(self, theta, axis_vec):
        cos = math.cos(theta)
        sin = math.sin(theta)

        axis = axis_vec / np.linalg.norm(axis_vec)

        nx = axis[0,0]
        ny = axis[1,0]
        nz = axis[2,0]

        print(nx,ny,nz)

        R = np.matrix([[cos+nx*nx*(1-cos), nx*ny*(1-cos)-nz*sin, nx*nz*(1-cos)+ny*sin],
                       [ny*nx*(1-cos)+nz*sin, cos+ny*ny*(1-cos), ny*nz*(1-cos)-nx*sin],
                       [nz*nx*(1-cos)-ny*sin, nz*ny*(1-cos)+nx*sin, cos+nz*nz*(1-cos)]])

        return R


if __name__ == '__main__':
    A = np.matrix([[1.],[0.],[0.]])
    B = np.matrix([[0.],[1.],[0.]])
    C = np.matrix([[0.],[0.],[1.]])

    a = np.matrix([[1.],[0.]])
    b = np.matrix([[0.],[1.]])

    CA = CalcAngle()
    # CA.rotation_to_zvec(A)
    CA.calc_cross(A,B)
    theta = CA.calc_corner(A,B)
    CA.rodrigues_rotation(theta, C)