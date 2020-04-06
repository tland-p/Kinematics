#!usr/bin/env python
# -*- coding:utf-8 -*-
import math

class JointAngles:
    def __init__(self):
        WRJ1_deg_x = 0
        WRJ2_deg_y = 0

        self.WRJ_SET_DEG = [WRJ1_deg_x, WRJ2_deg_y]

        FFJ3_deg_y = 0
        FFJ3_deg_x = 0
        FFJ2_deg_x = 0
        FFJ1_deg_x = 0

        self.FFJ_SET_DEG = [FFJ3_deg_y, FFJ3_deg_x, FFJ2_deg_x, FFJ1_deg_x]

        MFJ3_deg_y = 0
        MFJ3_deg_x = 0
        MFJ2_deg_x = 0
        MFJ1_deg_x = 0

        self.MFJ_SET_DEG = [MFJ3_deg_y, MFJ3_deg_x, MFJ2_deg_x, MFJ1_deg_x]

        RFJ3_deg_y = 0
        RFJ3_deg_x = 0
        RFJ2_deg_x = 0
        RFJ1_deg_x = 0

        self.RFJ_SET_DEG = [RFJ3_deg_y, RFJ3_deg_x, RFJ2_deg_x, RFJ1_deg_x]

        # LFJ4_deg_x = 0
        LFJ3_deg_y = 0
        LFJ3_deg_x = 0
        LFJ2_deg_x = 0
        LFJ1_deg_x = 0

        self.LFJ_SET_DEG = [LFJ3_deg_y, LFJ3_deg_x, LFJ2_deg_x, LFJ1_deg_x]

        # THJ
        THJ3_deg_z = 0
        THJ3_deg_x = 0
        THJ2_deg_x = 0
        THJ2_deg_y = 0
        THJ1_deg_y = 45

        self.THJ_SET_DEG = [THJ3_deg_z, THJ3_deg_x, THJ2_deg_x, THJ2_deg_y, THJ1_deg_y]


        rad = math.pi / 180
        self.WRJ_SET_RAD = []
        self.FFJ_SET_RAD = []
        self.MFJ_SET_RAD = []
        self.RFJ_SET_RAD = []
        self.LFJ_SET_RAD = []
        self.THJ_SET_RAD = []

        for i in xrange(len(self.WRJ_SET_DEG)):
            rad_data = self.WRJ_SET_DEG[i] * rad
            self.WRJ_SET_RAD.append(rad_data)

        for i in xrange(len(self.FFJ_SET_DEG)):
            rad_data = self.FFJ_SET_DEG[i] * rad
            self.FFJ_SET_RAD.append(rad_data)

        for i in xrange(len(self.MFJ_SET_DEG)):
            rad_data = self.MFJ_SET_DEG[i] * rad
            self.MFJ_SET_RAD.append(rad_data)

        for i in xrange(len(self.RFJ_SET_DEG)):
            rad_data = self.RFJ_SET_DEG[i] * rad
            self.RFJ_SET_RAD.append(rad_data)

        for i in xrange(len(self.LFJ_SET_DEG)):
            rad_data = self.LFJ_SET_DEG[i] * rad
            self.LFJ_SET_RAD.append(rad_data)

        for i in xrange(len(self.THJ_SET_DEG)):
            rad_data = self.THJ_SET_DEG[i] * rad
            self.THJ_SET_RAD.append(rad_data)

# if __name__ == '__main__':
#     angles = JointAngles()
#
#     print(angles.WRJ_SET_DEG)
#     print(angles.FFJ_SET_DEG)
#     print(angles.MFJ_SET_DEG)
#     print(angles.RFJ_SET_DEG)
#     print(angles.LFJ_SET_DEG)
#     print(angles.THJ_SET_DEG)
#
#     print(angles.WRJ_SET_RAD)
#     print(angles.FFJ_SET_RAD)
#     print(angles.MFJ_SET_RAD)
#     print(angles.RFJ_SET_RAD)
#     print(angles.LFJ_SET_RAD)
#     print(angles.THJ_SET_RAD)