#!/usr/bin/env python
"""find longest collatz chain."""


def evencol(n):
    """even col."""
    return int(n/2)


def oddcol(n):
    """odd col."""
    return (3 * n) + 1


def col(n):
    """return length of col chain."""
    global ITERS
    while n != 1:
        ITERS += 1
        if n % 2 == 0:
            return col(evencol(n))
        elif n % 2 != 0:
            return col(oddcol(n))
    return ITERS

BIGGEST = 2

# for i in range(1, 100000):
#    global ITERS
#    ITERS = 0
#    big = col(BIGGEST)
#    ITERS = 0
#    testing = col(i)
#    if testing > big:
#        BIGGEST = i

# print BIGGEST

for i in range(1, 1000000):
    ITERS = 0
    testing = col(i)
    ITERS = 0
    if testing > BIGGEST:
        BIGGEST = testing
        print i

print BIGGEST
