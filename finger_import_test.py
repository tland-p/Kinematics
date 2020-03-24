#!usr/bin/env python
import math

path = 'DataImport/20200228/all/all_45deg.txt'

f = open(path)

print(type(f))
# <class '_io.TextIOWrapper'>
f.close()

with open(path) as f:
    s = f.read()
    print(type(s))
    print(s)
    f.close()

