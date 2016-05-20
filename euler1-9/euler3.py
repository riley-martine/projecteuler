#!/usr/bin/env python
"""this script finds largest prime factor of that big number."""

from __future__ import division
import math


def isprime(factor):
    """check for primality."""
    for i in range(2, factor):
        if factor % i == 0:
            return False
    return True


def findfactor():
    """find factors of this number."""
    for i in range(2, int(math.sqrt(600851474143))):
        if 600851475143 % i == 0:
            if isprime(i):
                print i
            i -= 1
findfactor()
