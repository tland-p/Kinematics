#!usr/bin/env python
# -*- coding:utf-8 -*-
'''
This Program calc with FABRIK.
if you use, arg=pos(list) and arg=target(var)
'''
import math
import numpy as np
import scipy
import csv

from calc_modules.make_linkvec import make_linkvec
from calc_modules.calc_angle import CalcAngle
from calc_modules.make_matrix import MakeMatrix
from calc_modules.calc_plane_angle import xy_plane, quaternion_euler
from data.joint_positions import JointPositions

from forward_kinematics import ForwardKinematics

def convert_csv(data):  # make csv data about posset
    # pos = list(np.matrix([[],[],[]]))
    # make pos list
    pos = []

    for i in xrange(len(data)):
        pos3 = []
        line_vec = np.transpose(data[i])
        list_vec = line_vec.tolist()

        for j in xrange(len(list_vec)):
            pos.extend(list_vec[j])
            pos3.extend(list_vec[j])

        file_name = 'result/csv/thumb_calculated_with_FABRIK2.csv'
        with open(file_name, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(pos3)
            if i == len(data)-1:
                writer.writerow(' ')
                writer.writerow(' ')

    file_name = 'result/csv/thumb_calculated_with_FABRIK1.csv'
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(pos)
    # print(pos)

def convert_csv_init():
    file_name1 = 'result/csv/thumb_calculated_with_FABRIK1.csv'
    with open(file_name1, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['#THJ0x', 'THJ0y', 'THJ0z',
                         'THJ1x', 'THJ1y', 'THJ1z',
                         'THJ2x', 'THJ2y', 'THJ2z',
                         'THJ3x', 'THJ3y', 'THJ3z'])

    file_name2 = 'result/csv/thumb_calculated_with_FABRIK2.csv'
    with open(file_name2, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['#x', 'y', 'z'])


class FABRIK:
    def __init__(self, pos):
        self.pos = pos
        self.base = pos[0]
        self.n = len(pos) - 1
        self.linkvec = make_linkvec(pos)

    def backward(self, target):
        self.pos[self.n] = target

        for j in xrange(self.n):
            i = (self.n-1) - j
            r = np.linalg.norm(self.pos[i+1] - self.pos[i])
            l = np.linalg.norm(self.linkvec[i]) / r

            self.pos[i] = (1-l)*self.pos[i+1] + l*self.pos[i]
        # else:
            # print(self.linkvec)
            # print(self.pos)

    def forward(self):
        self.pos[0] = self.base

        for i in xrange(self.n):
            r = np.linalg.norm(self.pos[i+1] - self.pos[i])
            l = np.linalg.norm(self.linkvec[i]) / r

            self.pos[i+1] = (1-l)*self.pos[i]  + l*self.pos[i+1]

    def solve(self, target):
        tolerance = 0.01
        loop = 0
        link_length = 0

        for i in xrange(self.n):
            link_length =link_length + np.linalg.norm(self.linkvec[i])

        if np.linalg.norm(target) > link_length:
            print('check: unreachable')

            for i in xrange(self.n):
                r = np.linalg.norm(target - self.posset[i])
                l = np.linalg.norm(self.linkvec[i]) / r
                self.pos[i+1] = (1-l)*self.pos[self.n] - target

        else:
            print('check: reachable')
            error = np.linalg.norm(self.pos[self.n]-target)
            convert_csv(self.pos)

            while error > tolerance:

                self.backward(target)
                self.forward()
                error = np.linalg.norm(self.pos[self.n]-target)
                convert_csv(self.pos)

                if loop == 200:
                    print('loop reach 200 times')
                    break

                loop += 1

        return self.pos

if __name__ == '__main__':
    convert_csv_init()   # ファイルの初期化

    fk = ForwardKinematics()
    linkvec, fk_position, fk_main_vec, fk_sub_xvec, fk_sub_yvec = fk.forward_kinematics()

    positions = JointPositions()
    pos = positions.THJ_sets_pos
    # target1 = np.matrix([[0.],[20.],[40.]])
    # result = a.solve(target1)

    print(pos[0:3])
    a = FABRIK(pos[0:3])
    result = a.solve(fk_position[1])
    print(fk_position[1])

    with open('result/csv/target.csv', 'w') as f:
        target = []
        line_vec = np.transpose(fk_position[1])
        list_vec = line_vec.tolist()
        for j in xrange(len(list_vec)):
            target.extend(list_vec[j])

        writer = csv.writer(f)
        writer.writerow(['#target_x','target_y','target_z'])
        writer.writerow(target)

    ca = CalcAngle()
    '''
    check CalcAngle class with FABRIK result 'thj3'
    '''
    # print(type(pos[1]), type(result[1]))
    # print(np.linalg.norm(pos[1]), np.linalg.norm(result[1]))
    theta = ca.calc_corner(pos[1],result[1])
    vec = ca.calc_cross(pos[1],result[1])
    axis_vec = vec / np.linalg.norm(vec)
    Rthj3 = ca.rodrigues_rotation(theta, axis_vec)
    print(Rthj3)

    rotated = Rthj3 * pos[1]
    inv_rotated = Rthj3.T * result[1]
    print(rotated, result[1])
    print(pos[1], inv_rotated)

    ### 外積（回転軸）とx軸の角度からz軸周りの回転行列を求める
    ### MakeMatrixを使ってx,z軸回転で求める
    axis_x = np.matrix([[1.],[0.],[0.]])
    axis_z = np.matrix([[0.],[0.],[1.]])
    theta_around_z = ca.calc_corner(axis_x, axis_vec)  #ERROR!!
    # theta_around_z = math.radians(30)

    mm = MakeMatrix()
    '''
    '''
    Rthj3x = mm.make_x_matrix(theta)
    '''
    '''
    Rthj3z = mm.make_z_matrix(theta_around_z)
    rotated_with_axis = (Rthj3x * Rthj3z) * pos[1]
    inv_rotated_with_axis1 = Rthj3z.T * Rthj3x.T * result[1] # False
    inv_rotated_with_axis2 = Rthj3x.T * Rthj3z.T * result[1] # True

    print('check')
    print(rotated_with_axis, result[1])
    print(inv_rotated_with_axis1, inv_rotated_with_axis2)


    '''
    check CalcAngle class with FABRIK result 'thj2'
    '''
    rotated_pos2 = Rthj3 * pos[2] - result[1]
    result2 = result[2] - result[1]
    norm1 = np.linalg.norm(rotated_pos2)
    norm2 = np.linalg.norm(result2)
    print(norm1,norm2)
    theta2 = ca.calc_corner(rotated_pos2,result2)
    vec2 = ca.calc_cross(rotated_pos2, result2)
    axis_vec2 = vec2 / np.linalg.norm(vec2)
    Rthj2 = ca.rodrigues_rotation(theta2, axis_vec2)
    anglex, angley, Rtheta = quaternion_euler(theta2, axis_vec)
    Rx = mm.make_x_matrix(anglex)
    Ry = mm.make_y_matrix(angley)
    print(Rtheta, Rthj2)

    print(Rthj2, Ry*Rx)
    print('checked')
    print(math.degrees(anglex),math.degrees((angley)))

    rotated2 = result[1] + (Rthj2 * (pos[2] - pos[1]))
    inv_rotated2 = Rthj3.T * (result[1] + Rthj2.T * (result[2] - result[1]))
    print(rotated2, result[2])
    print(inv_rotated2, pos[2])

    # Answer: target = fk_position[1]
    # theta_around_z, theta, anglex, angley
    R3z = mm.make_z_matrix(theta_around_z)
    R3x = mm.make_x_matrix(theta)
    R2x = mm.make_x_matrix(anglex)
    R2y = mm.make_y_matrix(angley)

    print('ALL DEGREES')
    print(math.degrees(theta_around_z),math.degrees(theta),math.degrees(anglex),math.degrees(angley))

    print(linkvec)
    all_result = R3z * R3x * (linkvec[0] + R2y * R2x * (linkvec[1]))
    print(fk_position[1], all_result)



    # '''
    # ベクトルのなす角からローカル軸の回転に分解する
    # '''
    # main_vec = np.matrix([[0.],[0.],[1.]])
    # sub_yvec = np.matrix([[0.],[1.],[0.]])
    # sub_xvec = np.matrix([[1.],[0.],[0.]])
    #
    # R_before = Rthj3z * Rthj3x
    # a1_main = R_before * main_vec
    # ai_yvec = R_before * sub_yvec
    # a1_xvec = R_before * sub_xvec
    #
    # angle_x, angle_y = xy_plane(Rthj2)
    # Rthj2x = mm.make_x_matrix(angle_x)
    # Rthj2y = mm.make_y_matrix(angle_y)
    # rotated2_xy = result[1] + (Rthj2x * Rthj2y * (result[2] - result[1]))
    # rotated2_yx = result[1] + (Rthj2y * Rthj2x * (result[2] - result[1]))
    # print(rotated2, rotated2_yx, rotated2_xy)