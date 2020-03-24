#!usr/bin/env python
import math
import sys

class OpenFile:
    def __init__(self):
        self.path1 = 'DataImport/20200228/all/all_45deg.txt'

    def read_method(self):
        f = open(self.path1)
        