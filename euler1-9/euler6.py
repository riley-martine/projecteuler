#!/usr/bin/env python
"""
Find difference.

Diff between sum of squares of the first 100 nums and the square of their sum.
"""


SQUARED = 0
SUM = 0


for i in range(0, 101):
    SUM += i
    SQUARED += i**2

print SUM**2 - SQUARED
