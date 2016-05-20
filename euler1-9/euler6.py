#!/usr/bin/env python
"""find the difference between the sum of the squares of the first one hundred
natural numbers and the square of their sum"""


SQUARED = 0
SUM = 0


for i in range(0, 101):
    SUM += i
    SQUARED += i**2

print SUM**2 - SQUARED
