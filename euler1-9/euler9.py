#!/usr/bin/env python
"""finds pythagorean triplet a+b+c=1000."""


import math
C = 0


for a in range(1, 1000):
    for b in range(1, 1000 - a):
        C = (1000 - a - b)
        if math.sqrt(a**2 + b**2) == C:
            print '-----'
            print a
            print b
            print C
            print '-----'
            print a * b * C
            break
