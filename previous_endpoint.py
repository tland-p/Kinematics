#!usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import scipy

def previous_endpoint(endpoint, linkvec, mainvec):
    length = np.linalg.norm(linkvec)
    before_pos = endpoint - length * mainvec

    return before_pos