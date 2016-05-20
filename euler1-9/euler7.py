#!/usr/bin/env python
"""find 100001st prime."""


import math
PRIMECOUNT = 0
TESTING = 1


def isprime(num):
    """check for primality."""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

while 1 == 1:
    if isprime(TESTING):
        if PRIMECOUNT == 10001:
            break
        PRIMECOUNT += 1
    TESTING += 1
print TESTING
