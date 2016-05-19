#!/usr/bin/env python
"""this script finds the sum of even Fibbonacci numbers less than 4 million"""

from __future__ import division
FIB1 = 0
FIB2 = 1
TOTAL = 0
while FIB1 < 4000000 and FIB2 < 4000000:
    FIB1 += FIB2
    if (FIB1 / 2) % 1 == 0:
        TOTAL += FIB1
    FIB2 += FIB1
    if (FIB2 / 2) % 1 == 0:
        TOTAL += FIB2
print TOTAL
