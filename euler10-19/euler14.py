#!/usr/bin/env python
"""find longest callarz chain."""


def evencol(n):
    """even col."""
    return int(n/2)


def oddcol(n):
    """odd col."""
    return (3 * n) + 1


def col(n, COUNT):
    """return length of col chain."""
    if n == 1:
        return COUNT
    elif n % 2 == 0:
        col(evencol(n), COUNT + 1)
    elif n % 2 != 0:
        col(oddcol(n), COUNT + 1)
    return COUNT

for i in range(1, 10):
    COUNT = 1
    print col(i, COUNT)
