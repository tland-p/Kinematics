#!usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import scipy

def data_tp():
    path = 'DataImport/20200228/thumb/thumb_45deg.txt'
    delimeter=' '
    with open(path) as f:
        # data = [v.rstrip().stlip(delimiter) for v in f.readlines()]
        # data = f.read().split('\r\n')
        data_file = f.read().split()
        print(data_file)
        data = np.array(data_file).reshape(-1, 10)


        print(data[0,0])

    # print(datalist[0])
    f.close()

    return data