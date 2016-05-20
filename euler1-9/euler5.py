#!/usr/bin/env python
"""find smallest number evenly divisible by all nums 1-20"""

TESTING = 2


def divbyfirst20(checkint):
    """is the number divisible by nums 1-20"""
    for i in range(11, 20):
        if checkint % i != 0:
            return False
    return True

while 1 == 1:
    if divbyfirst20(TESTING):
        break
    TESTING += 2

print TESTING
