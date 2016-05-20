#!/usr/bin/env python
"""this script finds the sum of all multiples of 3 or 5 below 1k."""
from __future__ import division
TOTAL = 0
for i in range(0, 1000):
    if (i / 5) % 1 == 0:
        TOTAL += i
    elif (i / 3) % 1 == 0:
        TOTAL += i
print TOTAL
