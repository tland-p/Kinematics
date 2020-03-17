#!usr/bin/env python
# -*- coding:utf-8 -*-

def make_linkvec(pos):
    linkvec = []
    for i in xrange(len(pos) - 1):
        vec = pos[i + 1] - pos[i]
        linkvec.append(vec)

    return linkvec
